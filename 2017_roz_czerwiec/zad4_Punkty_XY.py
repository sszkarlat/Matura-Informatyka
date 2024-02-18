import math

t = []


def is_prime(i):
    if i < 2:
        return False
    else:
        for x in range(2, i):
            if i % x == 0:
                return False
    return True


def dlugosc(a, b):
    return int(round(math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2), 0))


licznik_prime = 0
licznik_cyfra = 0
licznik_wew = 0
licznik_bok = 0
licznik_zew = 0
max_dlugosc = 0
max_A = 0
max_B = 0

with open("punkty.txt", "r") as f:
    for l in f.read().splitlines():
        t.append((int(l.split()[0]), int(l.split()[1])))

for ws in t:
    if is_prime(ws[0]) and is_prime(ws[1]):
        licznik_prime += 1
    if sorted(set(list(str(ws[0])))) == sorted(set(list(str(ws[1])))):
        licznik_cyfra += 1
    if ws[0] < 5000 and ws[1] < 5000:
        licznik_wew += 1
    elif ws[0] == 5000 or ws[1] == 5000:
        licznik_bok += 1
    elif ws[0] > 5000 or ws[1] > 5000:
    # else:
        licznik_zew += 1

print(f"4.1: {licznik_prime}")

print(f"4.2: {licznik_cyfra}")

for i in range(len(t)):
    for l in range(i + 1, len(t)):
        # print(f"A={t[i]}, B={t[l]}, odleglosc={dlugosc(t[i], t[l])}")
        if dlugosc(t[i], t[l]) > max_dlugosc:
            max_dlugosc = dlugosc(t[i], t[l])
            max_A = t[i]
            max_B = t[l]

print("4.3:", max_A, max_B, max_dlugosc)
print(f"4.4: wewnatrz: {licznik_wew}, na boku: {licznik_bok}, zewnatrz: {licznik_zew}")
