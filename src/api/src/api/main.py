from time import time

from celery import chord, group
from fastapi import FastAPI
from starlette.responses import Response

from celeryworker.worker import add_two_numbers

app = FastAPI()

@app.get("/")
async def root() -> Response:
    """Root, can be used for liveliness probe

    Returns:
        A response with simple message
    """
    return {"msg":"Service running"}



@app.get("/add")
async def do_task() -> Response:
    """Run a task with celery workers

    Returns:
        A response with the results in the payload
    """

    s = time()

    job = group(add_two_numbers.s(i,i) for i in range(100))
    result = job.apply_async()
    
    result.ready()
    res = result.get()
    print(f'Took {time()-s} seconds.')

    return {"result":res}
