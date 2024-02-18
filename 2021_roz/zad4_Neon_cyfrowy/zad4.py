t = []
napis = []
with open("instrukcje.txt", "r") as f:
    for l in f.read().splitlines():
        t.append((l.split()[0], l.split()[1]))

slownik = {}
for i in range(65, 91):
    slownik[chr(i)] = 0
for l in t:
    instrukcja = l[0]
    litera = l[1]
    if instrukcja == "DOPISZ":
        napis.append(litera)
        slownik[litera] += 1
    elif instrukcja == "ZMIEN":
        napis[-1] = litera
    elif instrukcja == "USUN":
        napis.pop(-1)
    elif instrukcja == "PRZESUN":
        if litera == "Z":
            litera_p = "A"
        else:
            litera_p = chr(ord(litera) + 1)
        index = napis.index(litera)
        napis[index] = litera_p

instrukcje_tmp = []
instrukcje_max = []
for l in t:
    instrukcja = l[0]
    if not instrukcje_tmp:
        instrukcje_tmp.append(instrukcja)
    elif instrukcja in instrukcje_tmp:
        instrukcje_tmp.append(instrukcja)
        if len(instrukcje_tmp) > len(instrukcje_max):
            instrukcje_max = instrukcje_tmp.copy()
    else:
        instrukcje_tmp.clear()
        instrukcje_tmp.append(instrukcja)
max_wystapien = 0
max_litera = 0
for litera in slownik:
    if slownik[litera] > max_wystapien:
        max_litera = litera
        max_wystapien = slownik[litera]

print("Zadanie 4.1")
print(f"Długośc napisu: {len(napis)}")

print("\n""Zadanie 4.2")
print(f"Rodzaj instrukcji: {instrukcje_max[0]}, Długość ciągu: {len(instrukcje_max)}")

print("\n""Zadanie 4.3")
print(f"Litera: {max_litera}, Dopisywana: {max_wystapien} razy")

print("\n""Zadanie 4.4")
print("".join(napis))
