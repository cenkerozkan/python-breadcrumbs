lists_sample: list = [
    [1,2,3], [1,2,5,4], [7,9]
]

lenght_list: list = [len(i) for i in lists_sample]
print(min(lenght_list)) # This one gives the length of the shortest list.
print(min(lists_sample, key=len)) # This one gives the list itself