import time

from settings import settings

while True:
    time.sleep(1)

    print(settings.secret_text)
    print(settings.password)
    print(settings.min_number)
    print(settings.max_number)
