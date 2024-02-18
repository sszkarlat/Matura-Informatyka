licznik_K = 0
licznik_M = 0
with open("dane.txt") as f:
    for l in f.read().splitlines():
        if int(l[-2]) % 2 == 0:
            licznik_K += 1
        else:
            licznik_M += 1
print(licznik_K, licznik_M)