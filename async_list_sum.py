import asyncio

sample_input_1:list[list[int]] = [[1,2], [3,4]]
sample_input_2:list[list[int]] = [[1, 2, 2.3, 4, 5]] + [[3, 7, 3, 8, 15]] # Also with a plus
sample_input_3:list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def validate_lengths(input: list):
    sym_len: int = 0
    for i in input:
        if sym_len == 0:
            sym_len = len(i)
            continue
        if sym_len != len(i):
            raise ValueError("Every lists must have the same length.")

async def list_sum(input: list) -> list:
    validate_lengths(input)
    my_result: list = [0 for _ in range(len(input[0]))]
    for i in input:
        for j in range(len(i)):
            my_result[j] += i[j]
    return my_result

loop = asyncio.get_event_loop()
task_list = (list_sum(sample_input_1), list_sum(sample_input_2), list_sum(sample_input_3))
task_group = asyncio.gather(*task_list)