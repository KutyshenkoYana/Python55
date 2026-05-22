# pip install fastapi
# pip install "uvicorn[standard]"
# pip install pydantic


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# uvicorn MAINMAIN:app --host 127.0.0.1 --port 8000
# http://127.0.0.1:8000/docs


@app.get("/hello_endpoint")
def hello():
    return {"message": "hello world"}


@app.post("/register/{username}")
def register_user(username: str):
    return {
        "user": username,
        "is registered": True,
    }


# створеня схеми для данних

# дани користувача


class User(BaseModel):
    name: str
    age: int
    email: str


# @app.post("/register")
# def register(user: User):
#     print(user)
#
#     return {
#         "user_name": user.name,
#         "user_age": user.age,
#         "user_email": user.email,
#         "is_registered": True,
#     }


class UserResponse(BaseModel):
    user_name: str
    user_age: int
    user_email: str
    is_registered: bool


@app.post("/register")
def register(user: User) -> UserResponse:
    """
    Register user
    :param user:
    :return:
    """
    return UserResponse(
        user_name=user.name,
        user_age=user.age,
        user_email=user.email,
        is_registered=True,
    )


# put, delete, post, get
