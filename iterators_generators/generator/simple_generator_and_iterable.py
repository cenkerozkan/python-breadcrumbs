from abc import ABC
from collections import deque
from typing import Iterator, Iterable, Any, Generator

class SimpleIterable:
    def __init__ (self, iterable: list):
        self._data = iterable
        self._length = len(iterable)

    @property
    def length (self):
        return self._length

    @length.setter
    def length (self, value):
        self._length = value

    @length.getter
    def length (self):
        return self._length

    def pop(self, index: int):
        self._length -= 1
        if self._length > 0:
            return self._data.pop(index)
        return None

def iterator_method(iterable: SimpleIterable) -> Generator:
    while iterable.length > 0:
        pop_result: Any = iterable.pop(0)
        if pop_result is None:
            break
        yield pop_result

if __name__ == '__main__':
    iterable_obj = SimpleIterable([1, 2, 3, 4, 5])
    for i in iterator_method(iterable_obj):
        print(i)