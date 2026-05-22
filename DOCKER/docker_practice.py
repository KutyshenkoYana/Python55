import random
import time

while True:
    time.sleep(2)
    print(random.randint(0, 100))

# create build
# docker build -t [name build] [way to dockerfile]
# docker build -t random_num .
# kontrola   docker images
