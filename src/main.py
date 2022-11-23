from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from supervisely.app.fastapi import run_sync
import time
import asyncio
import functools
from threading import Thread, Event

app = FastAPI()


exit_event = Event()
thread = None


@app.on_event("startup")
def startup_event():
    global thread
    print("----> start")
    # long_task_sync()
    threaded_function = functools.partial(long_task_sync)
    thread = Thread(target=threaded_function)
    thread.start()


@app.on_event("shutdown")
def shutdown_event():
    exit_event.set()
    thread.join()
    print("----> stop")


def long_task_sync():
    print("long task sync")
    for i in range(100):
        if i == 10:
            raise ValueError("test")
        print(f"Iteration {i}")
        time.sleep(1)
        if exit_event.is_set():
            return


# long_task_sync()

# # # https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/
# @repeat_every(seconds=1, max_repetitions=1)
# async def long_task_async():
#     print("long task async")
#     for i in range(100):
#         print(f"Iteration {i}")
#         # time.sleep(1)
#         await asyncio.sleep(1)


# def long_task_sync():
#     print("long task sync")
#     for i in range(100):
#         print(f"Iteration {i}")
#         time.sleep(1)


# import os
# import time
# from dotenv import load_dotenv
# import supervisely as sly
# from async_asgi_testclient import TestClient
# from supervisely.app.fastapi.utils import run_sync
# from fastapi import BackgroundTasks
# import asyncio
# import concurrent.futures

# # load ENV variables for debug
# # has no effect in production
# load_dotenv("local.env")
# load_dotenv(os.path.expanduser("~/supervisely.env"))

# app = sly.Application()
# executor = concurrent.futures.ThreadPoolExecutor()


# @app.get_server().on_event("startup")
# def main():
#     # use only for initialization
#     print("Do something before initialization")
#     # loop = asyncio.get_event_loop()
#     # loop.create_task(long_task())

#     loop = asyncio.get_running_loop()
#     asyncio.ensure_future(loop.run_in_executor(executor, long_task))


# @app.get_server().on_event("shutdown")
# def stop():
#     print("Do something before stop")


# # @app.get_server().post("/items")
# def long_task():
#     for i in range(100):
#         print(f"Iteration {i}")
#         time.sleep(1)


# # client = TestClient(app)
# # resp = run_sync(client.post("/items"))
# # print("!!!!!!!!!!!!!!!!! ", resp)
