versions: list = ["1111.1.2", "2.3.41", "0.5.0", "2.312.5", "65.0.1"]
versions_inted_copy = [[int(i) for i in j.split(".") ] for j in versions]

sym_max: list | None = None
for i in versions_inted_copy:
    if sym_max is None:
        sym_max = i
    if i[0] > sym_max[0]:
        sym_max = i
    if i[0] == sym_max[0]:
        if i[1] > sym_max[1]:
            sym_max = i
        if i[1] == sym_max[1]:
            if i[2] > sym_max[2]:
                sym_max = i
print(str(".".join(str(i) for i in sym_max)))