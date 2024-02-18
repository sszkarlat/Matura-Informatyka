from collections import Counter

kody = []
galeria_lokale = []
galeria = []

with open("galerie_przyklad.txt", "r") as f:
    for l in f.read().splitlines():
        kody.append(l.split()[0])
        galeria_lokale.append(l.split()[1:])

# zad4.1
for kod in set(kody):
    print(kod, kody.count(kod))

kody2 = {}
for kod in kody:
    if kod in kody2:
        kody2[kod] += 1
    else:
        kody2[kod] = 1
print(kody2)

print(Counter(kody))

# zad 4.2
# galeria_powierzchnie = {}
# for i in galeria_lokale:
#     dane = i
#     powierzchnia_calkowita = 0
#     ilosc_lokali = 0
#     for l in range(1, len(dane) - 1, 2):
#         if dane[l] != "0":
#             powierzchnia_calkowita += int(dane[l]) * int(dane[l + 1])
#             ilosc_lokali += 1
#     # print(dane[0], powierzchnia_calkowita, ilosc_lokali)
#     galeria_powierzchnie[dane[0]] = powierzchnia_calkowita
#
# galeria_powierzchnia = sorted(galeria_powierzchnie.items(), key=lambda x: x[1])
# print(f"max = {galeria_powierzchnia[-1]}, min = {galeria_powierzchnia[0]}")

# zad 4.3
# powierzchnia = []
# licznik_tmp = 0
# licznik = 0
#
# for i in galeria_lokale:
#     dane = i
#     ilosc_lokali = 0
#     for l in range(1, len(dane)-1, 2):
#         if dane[l] != "0":
#             powierzchnia.append(int(dane[l]) * int(dane[l+1]))
#     print(set(powierzchnia))
#     print(dane[0], pow)
#
#     # print(dane[0], ilosc_restauracji)





