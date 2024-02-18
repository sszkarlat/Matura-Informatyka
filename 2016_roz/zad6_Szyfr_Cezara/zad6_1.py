def szyfruj(slowo, klucz):
    haslo = ""
    for znak in slowo:
        haslo += chr((ord(znak) + klucz - 65) % 26 + 65)
    return (haslo)


with open("dane_6_1.txt", "r") as f:
    for slowo in f.read().splitlines():
        with open("wyniki_6_1.txt", "a") as plik:
            plik.write(szyfruj(slowo, 107)+ "\n")


# print(szyfruj("INTERPRETOWANIE", 107))
