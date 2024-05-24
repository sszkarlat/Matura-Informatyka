liczby = []
with open("Dane-NF-2405\liczby_przyklad.txt") as f:
    for wiersz in f.readlines():
        wierszLista = []
        for liczba in wiersz.split():
            wierszLista.append(int(liczba))
        liczby.append(wierszLista)


pierwszyWiersz = liczby[0]
drugiWiersz = liczby[1]

licznik = 0
for liczba1 in pierwszyWiersz:
    for liczba2 in drugiWiersz:
        if liczba2 % liczba1 == 0:
            licznik += 1
            break

print(licznik)
