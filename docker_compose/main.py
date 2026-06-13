import random
import time

from settings import settings

while True:
    time.sleep(1)

    rand_num = random.randint(
        settings.start_range,
        settings.end_range,
    )
    print(f"Random word: {rand_num}")
    print(f"{settings.password = }")
    print(f"{settings.login = }")
