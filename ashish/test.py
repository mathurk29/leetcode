
# declare type of a and b such that they can be Either int or float
from typing import Union

NumberType = Union[int, float]


class NotANumberException(Exception):
    def __init__(self, varname, *args, **kwargs):
        self.varname = varname

        super().__init__(*args, **kwargs)


def multiply(a: NumberType, b: NumberType) -> NumberType:
    if not isinstance(a, NumberType):
        raise NotANumberException("some exception message", varname="a")
    if not not isinstance(b, NumberType):
        raise NotANumberException(varname="b")
    return a * b


# what is difference between raise and raise from
@app.get("/multiply")
def multiplier(a: Any, b: Any):
    try:
        multiply(2, "abcd")
    except NotANumberException as ex:
        raise HttpException(f"faield due to {ex.varname}") from ex



# Point(1, 2) + Point(2, 3)  = Point(3, 5)
class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other: "Point"):
        return Point(self.a + other.a , self.b + other.b)

# used in sql alchemy when declaring one to many, many to many models with base reference

class Parent(BaseModel):
    children: list["Children"]


class Children(BaseModel):
    parent: Parent



# what will happen in this iterator = Infinite
class MyIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        return

for _ in MyIterator():
    ...

# define range iterator
class Range:
    def __init__(self, start, stop, step=1):
        self.start  = start - 1
        self.stop = stop
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        self.start += self.step
        return self.start


# Context managers using decorators
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    try:
        yield "Something"
    except Exception as ex:
        print("Handled easily here")


class MyContextManager:
    def __enter__(self):
        return "Something"
    
    def __exit__(self, *args):
        print("Tricky to handle here")


with MyContextManager() as value:
    raise Exception

# Decorators ( create greeting decorator that takes name as an argument prints Hi before function executes and Bye after)

# what is wraps where it is used ?

from functools import wraps
def greeting(name): # where to take the decorator ka argument
    def outer(func): # where does decorated function come
        @wraps(func)
        def inner(*args, **kwargs): # what all arguments should it take 
            print(f"Hi {name}")
            res = func(*args, **kwargs) # how to capture result so that u can do something else after this
            print(f"Bye {name}")
            return res
        return inner
    return outer


@greeting("Ashish")
def multipyl(a, b):
    return a * b

# What is GIL ?
# How does GIL behave in multi processing ?
# What threads have of their own and what do they share ?

# what are two ways of creating threads
import threading
from time import sleep

def sleeper():
    current_thread = threading.get_ident()
    for i in range(5):
        print(i, current_thread)
        sleep(1)

t1 = threading.Thread(target=sleeper)
t2 = threading.Thread(target=sleeper)
t1.start()
t2.start()

for i in range(3):
    print(i, threading.current_thread().name)
    sleep(1)

# how to create threads with inheritance, also take custom args

class MyThread(threading.Thread):
    def __init__(self, arg1, arg2, *args, **kwargs):
        self.arg1 = arg1
        self.arg2 = arg2
        super().__init__(*args, **kwargs)
    
    def run(self):
        print("run ho gaya thread")

# multiprocssing communication : how does it happen ?
# multiprocess how can it be achieved.

# how do executors work ? ThreadPoolExecutor and ProcessPoolExecutor

# asycnio

# how is asynchronous programming different from multithreading: keyword - Cooperative multitasking
# what is task and future in asyncio
# what is an event loop
# how does asyncio.gather work
# how can u implement asynchronous programming for functions that are synchronous but i/o bound
