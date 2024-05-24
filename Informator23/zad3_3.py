class Przedzial:
    def __init__(self, pocz, kon, dlugosc=1):
        self.pocz = pocz
        self.kon = kon
        self.dlugosc = dlugosc


def zawierasie(e1, e2):
    return e2.pocz < e1.pocz and e1.kon < e2.kon


def krotszy(e1):
    return abs(e1.kon - e1.pocz)


def main():
    with open("DANE\dane3.txt", "r") as dane:
        przedzialy = []
        for line in dane:
            pocz, kon = map(int, line.split())
            przedzialy.append(Przedzial(pocz, kon))

    # Sortujemy przedziały względem długości
    przedzialy.sort(key=krotszy)

    # Dla i-tego przedziału liczymy maksymalną długość łańcuchów o początku w tym przedziale
    for i in range(1, len(przedzialy)):
        for j in range(i):
            if zawierasie(przedzialy[j], przedzialy[i]):
                if przedzialy[i].dlugosc < przedzialy[j].dlugosc + 1:
                    przedzialy[i].dlugosc = przedzialy[j].dlugosc + 1

    # Znajdujemy największą długość łańcucha
    maks = max(przedzial.dlugosc for przedzial in przedzialy)

    # Wypisujemy najlepszy
    print(maks)


if __name__ == "__main__":
    main()
