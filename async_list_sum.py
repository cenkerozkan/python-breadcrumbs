import asyncio
from time import time, sleep

sample_input_1:list[list[int]] = [[1,2], [3,4]]
sample_input_2:list[list[int]] = [[1, 2, 2.3, 4, 5]] + [[3, 7, 3, 8, 15]] # Also with a plus
sample_input_3:list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

async def validate_lengths(input: list):
    sym_len: int = 0
    for i in input:
        if sym_len == 0:
            sym_len = len(i)
            continue
        if sym_len != len(i):
            raise ValueError("Every lists must have the same length.")

async def list_sum(input: list) -> list:
    await asyncio.sleep(1)
    await validate_lengths(input)
    my_result: list = [0 for _ in range(len(input[0]))]
    for i in input:
        for j in range(len(i)):
            my_result[j] += i[j]
    return my_result

async def main():
    start_time = time()
    result = await asyncio.gather(list_sum(sample_input_1), list_sum(sample_input_2), list_sum(sample_input_3))
    end_time = time()
    print(f"Time taken: {end_time - start_time}")

asyncio.run(main())

###########################

def validate_lengths_sync(input: list):
    sym_len: int = 0
    for i in input:
        if sym_len == 0:
            sym_len = len(i)
            continue
        if sym_len != len(i):
            raise ValueError("Every lists must have the same length.")

def list_sum_sync(input: list) -> list:
    sleep(1)
    validate_lengths_sync(input)
    my_result: list = [0 for _ in range(len(input[0]))]
    for i in input:
        for j in range(len(i)):
            my_result[j] += i[j]
    return my_result

def main_sync():
    start_time = time()
    result_one = list_sum_sync(sample_input_1)
    result_two = list_sum_sync(sample_input_2)
    result_three = list_sum_sync(sample_input_3)
    end_time = time()
    print(f"Time taken: {end_time - start_time}")


main_sync()