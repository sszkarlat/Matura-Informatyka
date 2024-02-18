def znajdz_klucz(a, b):
    return (ord(b) - ord(a)) % 26


t = []
with open("dane_6_3.txt", "r") as f:
    for l in f.read().splitlines():
        t.append((l.split()[0], l.split()[1]))
with open("wyniki_6_3.txt", "w") as plik:
    for slowo_szyfrogram in t:
        slowo = slowo_szyfrogram[0]
        szyfrogram = slowo_szyfrogram[1]
        klucz = znajdz_klucz(szyfrogram[0], slowo[0])
        for i in range(1, len(slowo)):
            klucz_tmp = znajdz_klucz(szyfrogram[i], slowo[i])
            if klucz_tmp != klucz:
                plik.write(slowo + "\n")
                break

# print(znajdz_klucz("Z","A"))
