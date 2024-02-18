t = []

with open("dane.txt") as f:
    for l in f.read().splitlines():
        t.append(l.split())

licznik = 0
for i in range(320):
    licznik_tmp = 1
    for l in range(199):
        if t[l][i] == t[l + 1][i]:
            licznik_tmp += 1
        elif licznik_tmp > licznik:
            licznik = licznik_tmp
            licznik_tmp = 1
        else:
            licznik_tmp = 1
print(licznik)