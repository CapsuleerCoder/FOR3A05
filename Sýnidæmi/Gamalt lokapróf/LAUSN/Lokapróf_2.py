
fyrri = int(input("Hvar byrjar bilið ?"))
seinni = int(input("Hvar endar bilið ?"))

for i in range(fyrri, seinni+1):
    if i % 4 != 0 and i % 7 != 0:
        print(i)



