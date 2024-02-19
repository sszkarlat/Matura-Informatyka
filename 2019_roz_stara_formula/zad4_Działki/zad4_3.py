dzialki = []
dzialka = []
with open("dzialki.txt") as f:
    for i in f.read().splitlines():
        if i != "":
            dzialka.append(i)
        else:
            dzialki.append(dzialka)
            dzialka = []


def znalezieniePrzeszkod(dzialki):
    przeszkodyWszystkie = []
    for i in range(len(dzialki)):
        przeszkody = []
        dzialka = dzialki[i]
        for j in range(len(dzialka)):
            for k in range(len(dzialka[j])):
                if dzialka[j][k] == "X":
                    przeszkody.append((j, k))
        przeszkodyWszystkie.append(przeszkody)
    return przeszkodyWszystkie


def obliczaniePotencjalnychKwadratow(przeszkody):
    boki = []
    for przeszkoda in przeszkody:
        if przeszkoda[0] > przeszkoda[1]:
            bok = przeszkoda[0]
        else:
            bok = przeszkoda[1]
        boki.append(bok)
    return min(boki)


przeszkodyWszystkie = znalezieniePrzeszkod(dzialki)
bokDlaDzialki = {
    i + 1: obliczaniePotencjalnychKwadratow(przeszkodyWszystkie[i])
    for i in range(len(przeszkodyWszystkie))
}

maxBok = max(bokDlaDzialki.values())
print(f"Najdłuższy bok: {maxBok}")

for dzialka in bokDlaDzialki:
    if bokDlaDzialki[dzialka] == maxBok:
        print(f"Nr działki: {dzialka}")
