baris = 5
kolom = 5

for i in range(baris):
    for j in range(kolom):
        if i < j:
            print("9 ", end="")
        elif i == j:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()
