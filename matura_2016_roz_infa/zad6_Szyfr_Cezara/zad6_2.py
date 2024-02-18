def odszyfruj(slowo, klucz):
    haslo = ""
    for znak in slowo:
        haslo += chr((ord(znak) - klucz - 65) % 26 + 65)
    return (haslo)


t = []
with open("dane_6_2.txt", "r") as f:
    for l in f.read().splitlines():
        try:
            t.append((l.split()[0], int(l.split()[1])))
        except:
            print(l)

with open("wyniki_6_2.txt", "w") as f:
    for szyfrogram_klucz in t:
        f.write(odszyfruj(szyfrogram_klucz[0], szyfrogram_klucz[1]) + "\n")
