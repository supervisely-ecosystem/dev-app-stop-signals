import os
import time
from dotenv import load_dotenv
from art import tprint
import supervisely as sly
from async_asgi_testclient import TestClient
from supervisely.app.fastapi.utils import run_sync

# load ENV variables for debug
# has no effect in production
load_dotenv("local.env")
load_dotenv(os.path.expanduser("~/supervisely.env"))

app = sly.Application()


# def main():
# for i in range(100):
#     print(f"Iteration {i}")
#     time.sleep(1)


@app.get_server().on_event("startup")
def main():
    # use only for initialization
    print("Do something before initialization")


@app.get_server().on_event("shutdown")
def stop():
    print("Do something before stop")


client = TestClient(app)
resp = run_sync(client.get("/"))

# for i in range(100):
#     print(f"Iteration {i}")
#     time.sleep(1)
