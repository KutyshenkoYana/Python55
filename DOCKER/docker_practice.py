import random
import time

while True:
    time.sleep(2)
    print(random.randint(0, 100))

# create build
# docker build -t [name obrazu] [way to dockerfile]
# docker build -t random_num .
# kontrola   docker images
# docker run -d --name rand1 random_num   (rand1 - name) ,
# docker run --name rand2 random_num
# docker run [-d] --name [name obrazu] [name container]
# info   docker ps
# info about container   docker logs

# docker build -t fastapi_app .

# pip freeze > requirements.txt - all my installed library
