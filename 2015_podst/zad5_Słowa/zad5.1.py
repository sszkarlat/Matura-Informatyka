t = []
with open("slowa.txt", "r") as f:
    for l in f.read().splitlines():
        t.append(len(l))

for i in range(1, 13):
    print(i, t.count(i))
