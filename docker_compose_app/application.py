from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_endpoint")
def hello():
    return {
        "message": "hello",
        "status": "ok",
    }
