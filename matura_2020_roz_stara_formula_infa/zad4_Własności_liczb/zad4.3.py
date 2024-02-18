t = []
with open("dane_przyklad.txt", "r") as f:
    for i in f.read().splitlines():
        t.append(list(set(i)))
    # print(t)
licznik = 0
for x in t:
    tmp = []
    tmp.append(x)
    print(tmp)
    if tmp == x:
        print(tmp)

