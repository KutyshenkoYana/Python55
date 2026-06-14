import json

import pydantic
from fastapi import FastAPI
from settings import settings

app = FastAPI()


class Book(pydantic.BaseModel):
    id: int
    title: str
    author: str
    year: int
    pages: int


@app.get("/books")
def get_all_books() -> list[Book]:
    with open(settings.data_file_path) as f:
        books = json.load(f)
        return books


@app.get("/books/{id}")
def get_book(id: int) -> Book:
    with open(settings.data_file_path) as f:
        books = json.load(f)

    for book in books:
        if book["id"] == id:
            return book


@app.post("/books")
def create_book(book: Book) -> dict[str, str]:
    with open(settings.data_file_path) as f:
        books = json.load(f)

    books.append(book.model_dump())
    with open(settings.data_file_path, "w") as f:
        json.dump(books, f, indent=4)
    return {"message": "Book added"}
