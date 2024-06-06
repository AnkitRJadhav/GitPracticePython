print("Change from First Branch")
rows = int(input("Enter total rows: "))
for i in range(rows):
    for j in range(i):
        print("\t", end="")
    for k in range(rows+rows-i-i-1):
        print("*", end="\t")
    print("\n")
