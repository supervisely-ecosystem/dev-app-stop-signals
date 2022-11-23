import os
import time
from dotenv import load_dotenv
import supervisely as sly
from async_asgi_testclient import TestClient
from supervisely.app.fastapi.utils import run_sync
from fastapi import BackgroundTasks
import asyncio
import concurrent.futures

# load ENV variables for debug
# has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

app = sly.Application()
executor = concurrent.futures.ThreadPoolExecutor()


@app.get_server().on_event("startup")
def main():
    # use only for initialization
    print("Do something before initialization")
    # loop = asyncio.get_event_loop()
    # loop.create_task(long_task())

    loop = asyncio.get_running_loop()
    asyncio.ensure_future(loop.run_in_executor(executor, long_task))


@app.get_server().on_event("shutdown")
def stop():
    print("Do something before stop")


# @app.get_server().post("/items")
def long_task():
    for i in range(100):
        print(f"Iteration {i}")
        time.sleep(1)


# client = TestClient(app)
# resp = run_sync(client.post("/items"))
# print("!!!!!!!!!!!!!!!!! ", resp)
