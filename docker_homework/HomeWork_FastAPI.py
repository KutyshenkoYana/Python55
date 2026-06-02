# Завдання 1
# Напишіть сервер для збереження даних про фільми. Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними: id , title , director , year
# Функціонал:
# 1. Отримання даних за ID фільму
# ○ шлях – movies/{movie_id}
# ○ метод – GET

# 2. Додавання нового фільму
# ○ шлях – movies
# ○ метод – POST

# 3. Видалення фільму за ID
# ○ шлях – movies/{movie_id}
# ○ метод – DELETE
# Запустіть сервер

# Напишіть клієнта з таким фуннкціоналом для
# користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм


import json

import pydantic
from fastapi import FastAPI

app = FastAPI()


class Movie(pydantic.BaseModel):
    id: int
    title: str
    director: str
    year: int


@app.get("/movies/{id}")
def get_movie(id: int) -> Movie:
    with open("films.json", encoding="utf-8") as f:
        movies = json.load(f)

    for movie in movies:
        if movie["id"] == id:
            return movie


@app.post("/movies")
def create_movie(movie: Movie) -> dict[str, str]:
    with open("films.json", encoding="utf-8") as f:
        movies = json.load(f)

    movies.append(movie.model_dump())
    with open("films.json", "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)
        return {"message": "movie added"}


@app.delete("/movies/{id}")
def delete_movie(id: int) -> dict[str, str]:
    with open("films.json", encoding="utf-8") as f:
        movies = json.load(f)

    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)

            with open("films.json", "w", encoding="utf-8") as f:
                json.dump(movies, f, indent=4)

            return {"message": "movie deleted"}

    return {"message": "movie not found"}
