import sys
from time import time
from typing import Callable


def return_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print("--------------")
        start = time()
        func(*args, **kwargs)
        print(f"Passed time: {time() - start} name: {func.__name__}")

    return wrapper


@return_time
def func1(exp: int = 6):
    result2 = (i for i in range(0, 10**exp))
    # print(len(result2))
    print(sys.getsizeof(result2) / 1024)


@return_time
def func2(exp: int = 6):
    result: list = [i for i in range(0, 10**exp)]
    print(sys.getsizeof(result) / 1024)


# func1()
# func2()

func1(7)
func2(7)
