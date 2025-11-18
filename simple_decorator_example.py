from time import time, sleep


def calc_time(multiplier: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            start = time()
            func(*args, **kwargs)
            end = time()
            print(f"Multiplied by {multiplier} time: {end - start}")
            print(f"{func.__name__} took {end - start} seconds")

        return wrapper

    return inner


@calc_time(multiplier=5)
def some_func(sleep_time: float):
    sleep(sleep_time)


some_func(1)
