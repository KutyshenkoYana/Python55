#python version
FROM python:3.14-slim

#basic folder
WORKDIR app

#copy files
#(copy all files)
COPY ./ ./

#install library
RUN pip install -r requirements.txt

#open port
EXPOSE 8080

#command to run
CMD ["python", "main.py"]
