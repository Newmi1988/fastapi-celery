import os
from random import randrange
from time import sleep

from celery import Celery

# check if the application is run outside of a docker
if "ISPRODUCTION" not in list(os.environ.keys()):
    app = Celery('tasks', backend = 'redis://localhost', broker='amqp://localhost')
else:
    app = Celery('tasks', backend = 'redis://redis', broker='amqp://rabbitmq')

@app.task(name="add.two")
def add_two_numbers(x : int,y : int) -> int:
    """Add to numbers with random delay.

    Args:
        x : a number
        y : another number

    Returns:
        Sum of the numbers
    """
    # sleep(randrange(3))
    print(f" Result is {x+y}")
    return x+y


