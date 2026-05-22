# run fastapi with uvicorn

# uvicorn MAINMAIN:app --host 127.0.0.1 --port 8000

import uvicorn

uvicorn.run(
    "application:app",
    host="127.0.0.1",
    port=8080,
    reload=True,
)
