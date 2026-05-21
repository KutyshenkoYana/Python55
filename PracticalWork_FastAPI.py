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

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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


class GreetingResponse(BaseModel):
    message: str


@app.get("/greeting")
def hello() -> GreetingResponse:
    return GreetingResponse(
        message="Hello from Server!",
    )
