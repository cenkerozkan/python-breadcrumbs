def return_list(empty: bool):
    return [] if not empty else [1]

if a := return_list(True):
    print("AAA")
else:
    print("BBB")

print(a)