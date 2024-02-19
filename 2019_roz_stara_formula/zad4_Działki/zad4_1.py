powDzialki = 30*30
trawa = "*"
dzialki = []
dzialka = []

with open("przyklad.txt") as f:
    for i in f.read().splitlines():
        if i != "":
            dzialka.append(i)
        else:
            dzialki.append(dzialka)
            dzialka = []

trawiasteDzialki = 0
for dzialka in dzialki:
    licznikTrawy = 0
    for wiersz in dzialka:
        licznikTrawy += wiersz.count(trawa)

    if (licznikTrawy / powDzialki) * 100 >= 70:
        trawiasteDzialki += 1

print(f"Dzialki, w 70% pokryte trawa: {trawiasteDzialki}")
