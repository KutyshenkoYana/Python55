FROM python:3.11-slim

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt

ENV MIN_NUMBER=0

CMD ["python", "-u", "main.py"]


#docker run -e PASSWORD=lalala --name app1
