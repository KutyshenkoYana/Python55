from fastapi import FastAPI

app = FastAPI()


# class GreetingResponse(BaseModel):
#     message: str
#
#
# @app.get("/greeting")
# def hello() -> GreetingResponse:
#     return GreetingResponse(
#         message="Hello from Server1!",
#     )
