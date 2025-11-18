from abc import ABC
from collections import deque
from typing import Iterator, Iterable, Any


class SimpleIterable:
    def __init__(self, iterable: list):
        self._data = iterable
        self._length = len(iterable)

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @length.getter
    def length(self):
        return self._length

    def pop(self, index: int):
        self._length -= 1
        if self._length > 0:
            return self._data.pop(index)
        return None


class SimpleListIterator:
    def __init__(self, iterable_list: SimpleIterable):
        self._iterable: SimpleIterable = iterable_list

    def _is_exhausted(self) -> bool:
        if self._iterable.length == 0:
            return True
        return False

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> Any:
        if self._is_exhausted():
            raise StopIteration
        pop_result = self._iterable.pop(0)
        if pop_result is None:
            raise StopIteration
        return pop_result


if __name__ == "__main__":
    iterable_obj = SimpleIterable(list([number for number in range(500)]))
    for item in SimpleListIterator(iterable_obj):
        print(item)
