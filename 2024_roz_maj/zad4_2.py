liczby = []
with open("Dane-NF-2405\liczby_przyklad.txt") as f:
    for wiersz in f.readlines():
        wierszLista = []
        for liczba in wiersz.split():
            wierszLista.append(int(liczba))
        liczby.append(wierszLista)

pierwszyWiersz = liczby[0]
pierwszyWiersz = sorted(pierwszyWiersz, reverse='True')
print(pierwszyWiersz[100])
