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

print(* sorted(dlugosci)[:2])
