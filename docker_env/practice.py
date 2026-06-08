import time

from settings import settings

while True:
    time.sleep(2)

    print(settings.password)
    print(settings.filename)
    print(settings.login)
    print(settings.app_name)
