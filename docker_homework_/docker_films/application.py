import json

import pydantic
from fastapi import FastAPI
from settings import settings

app = FastAPI()


class Movie(pydantic.BaseModel):
    id: int
    title: str
    director: str
    year: int


@app.get("/movies/{id}")
def get_movie(id: int) -> Movie:
    with open(settings.data_file_path, encoding="utf-8") as f:
        movies = json.load(f)

    for movie in movies:
        if movie["id"] == id:
            return movie


@app.post("/movies")
def create_movie(movie: Movie) -> dict[str, str]:
    with open(settings.data_file_path, encoding="utf-8") as f:
        movies = json.load(f)

    movies.append(movie.model_dump())
    with open(settings.data_file_path, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)
        return {"message": "movie added"}


@app.delete("/movies/{id}")
def delete_movie(id: int) -> dict[str, str]:
    with open(settings.data_file_path, encoding="utf-8") as f:
        movies = json.load(f)

    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)

            with open(settings.data_file_path, "w", encoding="utf-8") as f:
                json.dump(movies, f, indent=4)

            return {"message": "movie deleted"}

    return {"message": "movie not found"}
