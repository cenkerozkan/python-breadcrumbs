"""A custom implementation of the reduce function using iter() and next()."""


def add(x, y):
    return x + y


def custom_reduce(iterable, func):
    it = iter(iterable)
    result = next(it)
    while True:
        try:
            val = next(it)
            result = func(result, val)
        except StopIteration:
            return result


print(custom_reduce([1, 2], add))
