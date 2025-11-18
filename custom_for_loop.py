from typing import Container, Callable

"""A custom implementation of a for loop using iter() and next()."""

sample_string = "abcde"

def custom_for(container: Container, func: Callable) -> None:
    cont_iter = iter(container)
    while True:
        try:
            func(next(cont_iter))
        except StopIteration as e:
            print(str(e))
            break

custom_for(sample_string, print)
custom_for([1,2,3,4], print)
custom_for((1,2,3,4,5), print)
custom_for(range(1,125,25), print)
custom_for((i for i in range(1,5)), print)