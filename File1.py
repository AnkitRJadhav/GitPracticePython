rows = int(input("Enter total rows: "))
for i in range(rows):
    for j in range(rows-i):
        print("\t", end="")
    for k in range(i+i+1):
        print("*", end="\t")
    print("\n")
