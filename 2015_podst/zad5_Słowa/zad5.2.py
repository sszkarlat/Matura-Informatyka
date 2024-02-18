nowe = []
with open("nowe.txt", "r") as f:
    for l in f.read().splitlines():
        nowe.append(l)

slowa = []
with open("slowa.txt", "r") as f:
    for l in f.read().splitlines():
        slowa.append(l)

for i in nowe:
    print(i, slowa.count(i), slowa.count(i[::-1]))
