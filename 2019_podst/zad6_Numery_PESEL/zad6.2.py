licznik = 0
with open("dane.txt") as f:
    for l in f.read().splitlines():
        if l[2:4] in ("11", "31"):
            licznik += 1
print(licznik)
