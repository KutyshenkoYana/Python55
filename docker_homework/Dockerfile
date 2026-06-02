FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["uvicorn", "HomeWork_FastAPI:app", "--host", "0.0.0.0", "--port", "8080"]


#(.venv) PS C:\Users\jkuty\OneDrive\Documents\nNEW\docker_homework> docker ps
#CONTAINER ID   IMAGE           COMMAND                  CREATED          STATUS          PORTS                                         NAMES
#99c55e8a7583   movies          "uvicorn HomeWork_Fa…"   8 seconds ago    Up 6 seconds    0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   movies-container
#de23b79bfa80   pydantic-loop   "python -u main.py"      14 minutes ago   Up 14 minutes                                                 movies1
#7d2109a029c2   pydantic-loop   "python -u main.py"      45 minutes ago   Up 45 minutes                                                 test2
#(.venv) PS C:\Users\jkuty\OneDrive\Documents\nNEW\docker_homework> docker logs movies-container
#INFO:     Started server process [1]
#INFO:     Waiting for application startup.
#INFO:     Application startup complete.
#INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
