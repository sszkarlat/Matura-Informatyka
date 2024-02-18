def kodujBCD(a):
    wynik = ""
    while True:
        cyfra = ""
        c = a % 10
        a //= 10
        cyfra += chr(((c & 8) >> 3) + 48)
        cyfra += chr(((c & 4) >> 2) + 48)
        cyfra += chr(((c & 2) >> 1) + 48)
        cyfra += chr(((c & 1) >> 0) + 48)
        wynik = cyfra + wynik
        if a == 0:
            break
    return wynik


with open("binarne.txt", "r") as f:
    liczby = f.read().splitlines()

dwucykliczne = []
for liczba in liczby:
    if liczba[:len(liczba) // 2] == liczba[len(liczba) // 2:]:
        dwucykliczne.append(liczba)

slownik = {
    liczba: len(liczba)
    for liczba in dwucykliczne
}

for l in slownik:
    if slownik[l] == 32:
        najdluzszy_napis = l
liczby_dziesietne = []
for liczba in liczby:
    if int(liczba, 2) <= 65535:
        liczby_dziesietne.append((int(liczba, 2), liczba))

print("Zadanie 4.1")
print(f"Ilość napisów: {len(dwucykliczne)}, Najdłuższy napis: {najdluzszy_napis}, Długość: {len(najdluzszy_napis)}")

print("\n""Zadanie 4.3")
print(max(liczby_dziesietne))
