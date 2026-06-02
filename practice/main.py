import datetime
import sys
import time

import pydantic

start_time = datetime.datetime.now()

while True:
    time.sleep(2)
    print(f"Version_sys:{sys.version}")
    print(f"Version_pydantic:{pydantic.version}")
    print(f"Program started:{start_time}")
    print("Hello")
