dzialki = []
dzialka = []
with open("przyklad.txt") as f:
    for i in f.read().splitlines():
        if i != "":
            dzialka.append(i)
        else:
            dzialki.append(dzialka)
            dzialka = []

lista = []
for i in range(len(dzialki)):
    dzialka = dzialki[i]
    print(dzialka)
    for j in range(i + 1, len(dzialki) - 1):
        k1 = 0
        k2 = len(dzialki[i]) - 1

        while dzialka[k1] == dzialki[j][k2][::-1]:
            k1 += 1
            print(k1)
            k2 -= 1
            print(k2)

            if (k1 == len(dzialka) and k2 == -1):
                lista.append((i + 1, j + 1))
                break

print(lista)
