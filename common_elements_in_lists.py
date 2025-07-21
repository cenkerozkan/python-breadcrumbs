lists_sample: list = [[1,2,3], [1,2,5], [1,8,9]]

list_of_sets = [set(list) for list in lists_sample]
print(list_of_sets)

common_elements: set | None = list_of_sets[0] | set()
for i in list_of_sets:
    # if set is empty.
    if common_elements is None:
        common_elements = i
        continue
    common_elements &= i