# liczby = []
# with open("Dane-NF-2405\liczby_przyklad.txt") as f:
#     for wiersz in f.readlines():
#         wierszLista = []
#         for liczba in wiersz.split():
#             wierszLista.append(int(liczba))
#         liczby.append(wierszLista)

# pierwszyWiersz = liczby[0]
# # print(len(pierwszyWiersz))

# maxSrednia = 0
# maxFragment = []

# for i in range(len(pierwszyWiersz) - 50 + 1):
#     fragment = pierwszyWiersz[i: i + 50]
#     # print(fragment)
#     # print(len(fragment))
#     for j in range(i + 50, len(pierwszyWiersz) + 1):
#         srednia = sum(fragment) / (j - 1)
#         # print(i, srednia)
#         if srednia > maxSrednia:
#             maxSrednia = srednia
#             maxFragment = fragment
#         if j < len(pierwszyWiersz):
#             fragment.append(pierwszyWiersz[j])
#         # print(fragment)
#         # print(len(fragment))

# print(maxSrednia, len(maxFragment), maxFragment[0])


liczby = []
with open("Dane-NF-2405/liczby_przyklad.txt") as f:
    for wiersz in f.readlines():
        wierszLista = [int(liczba) for liczba in wiersz.split()]
        liczby.append(wierszLista)

pierwszyWiersz = liczby[0]
maxSrednia = 0
maxFragment = []
rozmiarFragmentu = 50

for i in range(len(pierwszyWiersz) - rozmiarFragmentu + 1):
    fragment = pierwszyWiersz[i: i + rozmiarFragmentu]

    for j in range(i + rozmiarFragmentu, len(pierwszyWiersz) + 1):
        srednia = sum(fragment) / len(fragment)

        if srednia > maxSrednia:
            maxSrednia = srednia
            maxFragment = fragment

        if j < len(pierwszyWiersz):
            fragment.append(pierwszyWiersz[j])

print(maxSrednia, len(maxFragment), maxFragment[0])
