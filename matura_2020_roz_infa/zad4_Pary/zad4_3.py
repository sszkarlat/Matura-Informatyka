min = "vfffffffffffddv" * 10
with open("Dane_PR2/pary.txt") as f:
    for l in f.read().splitlines():
        liczba = int(l.split()[0])
        slowo = l.split()[1]
        if liczba == len(slowo):
            if liczba < len(min):
                min = slowo
            elif liczba == len(min) and slowo < min:
                min = slowo
print(len(min), min)
