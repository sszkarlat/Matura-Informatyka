with open("przyklad.txt") as f:
    slowa = f.read().splitlines()

for slowo in slowa:
    flag = True
    for litera1 in slowo:
        for litera2 in slowo:
            if abs(ord(litera1) - ord(litera2)) > 10:
                flag = False
    if flag is True:
        print(slowo)
