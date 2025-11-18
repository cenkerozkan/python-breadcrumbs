"""
This is a simple iterator example that takes
"""

from typing import Iterable


class SimpleIterator:
    def __init__(self, length: int = 10):
        self._list: list[int] = [number for number in range(length)]

    def _is_exhausted(self) -> bool:
        if len(self._list) == 0:
            return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        # Iterators are exhaustive, so we need to check
        # if the exhausted all the data.
        # This one is an example from AsyncPyMongo library.
        if self._is_exhausted():
            raise StopIteration
        return self._list.pop(0)


if __name__ == "__main__":
    obj = SimpleIterator(length=120)
    obj_iterator = iter(obj)
    for i in obj_iterator:
        print(i)

    # Giving this iterator into a list comprehension
    iterated_list: list[int] = [number for number in SimpleIterator(length=120)]
    print(iterated_list)
