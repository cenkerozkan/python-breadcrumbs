# Given status -> coordinate dict
# Revert it to coordinate -> status dict
from pprint import pprint

status_point_dict: dict = {
    "occupied": [(1, 1), (0, 1), (1, 2)],
    "available": [(0, 0), (2, 1)],
    "unknown": [(1, 0), (0, 2), (2, 2), (2, 0)],
    "visited": [(0, 0), (1, 2), (1, 1)],
    "visit_planned": [],
}


def find_unique_tuples(data: dict) -> set[tuple]:
    value_set: set = set()
    for value in data.values():
        for i in value:
            value_set.add(i)
    return value_set


def shitty_mapping(data: dict, tuples: set[tuple]) -> list[tuple]:
    shitty_map: list[tuple] = []
    for value in tuples:
        temp_keys = []
        for key in data.keys():
            if value in data[key]:
                temp_keys.append(key)
        shitty_map.append(tuple((value, temp_keys)))
    for key in data.keys():
        if len(data[key]) == 0:
            shitty_map.append(tuple((key,)))
    return shitty_map


def reverse_dict(data: dict) -> dict:
    unique_tuples: set[tuple] = find_unique_tuples(data)
    shitty_map: list[tuple] = shitty_mapping(status_point_dict, unique_tuples)
    reversed_data: dict = {}
    for data in shitty_map:
        if len(data) == 1:
            reversed_data.update({tuple(): [data[0]]})
        else:
            reversed_data.update({data[0]: data[1]})
    return reversed_data


# print(find_unique_tuples(status_point_dict))
print(shitty_mapping(status_point_dict, find_unique_tuples(status_point_dict)))
result_one = reverse_dict(status_point_dict)
pprint(result_one)

result_two = reverse_dict(result_one)
pprint(result_two)
