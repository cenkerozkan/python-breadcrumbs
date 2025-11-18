sample_string: str = "This text has repeating chars."


# Shitty solution.
def find_first_non_repeating_char(sample_string) -> None:
    for i in range(0, len(sample_string)):
        is_repeated: bool = False
        for j in range(i + 1, len(sample_string)):
            if sample_string[i] == sample_string[j]:
                is_repeated = True
            if j == len(sample_string) - 1 and not is_repeated:
                print(f"First non repeating char: {sample_string[i]}")
                return


find_first_non_repeating_char(sample_string.lower())

# Better solution.
i_my_text = sample_string.casefold()
for i, j in enumerate(i_my_text):
    if j not in i_my_text[i + 1 :]:
        print(j)
        break
