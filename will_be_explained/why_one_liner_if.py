state: bool = False
numbers: list = [
    number * 100 if number % 2 == 0 else number * 10 for number in range(1, 10) if state
]
print(numbers)
