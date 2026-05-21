from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class GreetingResponse(BaseModel):
    message: str


@app.get("/greeting")
def hello() -> GreetingResponse:
    return GreetingResponse(
        message="Hello from Server1!",
    )
