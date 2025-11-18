"""
Question: Create a list with list comprehension from numbers 1 to 10
    * if number is even, multiply by 100
    * if number is odd, multiply by 10
"""


def create_list_comprehension() -> list:
    numbers: list = [
        number * 100 if number % 2 == 0 else number * 10 for number in range(1, 10)
    ]
    return numbers


print(create_list_comprehension())
