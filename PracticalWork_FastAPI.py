# Завдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер

# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()


# class Response(BaseModel):
#     message: str
#
#
# @app.post("/hello")
# def hello() -> Response:
#     return Response(
#         message="Hello!",
#     )

# uvicorn PracticalWork_FastAPI(1):app --port 8000 --host localhost --reload


# Завдання 2
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва
# сервери


# class GreetingResponse(BaseModel):
#     message: str
#
#
# @app.get("/greeting")
# def hello() -> GreetingResponse:
#     return GreetingResponse(
#         message="Hello from Server!",
#     )


# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET

# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET

# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST

# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE

import json

import pydantic
from fastapi import FastAPI

app = FastAPI()


class Book(pydantic.BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


@app.get("/books")
def get_all_books() -> list[Book]:
    with open("books.json") as f:
        books = json.load(f)
        return books


@app.get("/books/{id}")
def get_book(id: int) -> Book:
    with open("books.json") as f:
        books = json.load(f)

    for book in books:
        if book["id"] == id:
            return book


@app.post("/books")
def create_book(book: Book) -> dict[str, str]:
    with open("books.json") as f:
        books = json.load(f)

    books.append(book.model_dump())
    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)
    return {"message": "Book added"}
