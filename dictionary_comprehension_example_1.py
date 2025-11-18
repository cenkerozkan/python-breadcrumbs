"""
Question: Provide a dictionary according to following rules:
    * With numbers from 0 to 201
    * Number has to be multiple of 3 and 4
    * If number (key) is multiple of 3, value: Fizz
    * if number (key) is multiple of 5, value: FizzBuzz
"""

from pprint import pprint


def generate_dictionary_one_liner() -> dict:
    dictionary = {
        f"{i}": f"{'FizzBuzz' if i % 5 == 0 else 'Fizz'}"
        for i in range(1, 201)
        if i % 3 == 0 and i % 4 == 0
    }
    return dictionary


def generate_dictionary_one_liner_2() -> dict:
    dictionary = {
        f"{i}": f"{'FizzBuzz' if i % 5 == 0 else 'Fizz'}" for i in range(0, 201, 12)
    }
    return dictionary


pprint(generate_dictionary_one_liner())
pprint(generate_dictionary_one_liner_2())
