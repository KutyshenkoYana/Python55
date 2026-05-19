# pip install fastapi
# pip install "uvicorn[standard]"
# pip install pydantic


from fastapi import FastAPI

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
