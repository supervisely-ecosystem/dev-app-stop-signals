from fastapi import FastAPI
import time
import functools
from threading import Thread, Event

app = FastAPI()


exit_event = Event()
thread = None


@app.on_event("startup")
def startup_event():
    global thread
    print("----> start")
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
