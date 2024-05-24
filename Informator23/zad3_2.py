listaPar = []

with open("DANE\dane3.txt") as f:
    pary = f.read().splitlines()

    for para in pary:
        listaPara = []
        for liczba in para.split(" "):
            listaPara.append(int(liczba))

        listaPar.append(listaPara)

dlugosci = [
    abs(para[0] - para[1]) + 1
    for para in listaPar
]

dlugosciSlownik = {
    dlugosc: dlugosci.count(dlugosc)
    for dlugosc in dlugosci
}

maxDlugosc = max(dlugosciSlownik.values())
maxLiczba = 0
for dlugosc in dlugosciSlownik:
    if dlugosciSlownik[dlugosc] == maxDlugosc and dlugosc > maxLiczba:
        maxLiczba = dlugosc

print(maxLiczba, maxDlugosc)
