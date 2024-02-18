def pierwsza(x):
    pierwsze = []
    for n in range(2, x):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            pierwsze.append(n)
    return pierwsze


with open("Dane_PR2/pary.txt") as f:
    # licznik = 0
    for l in f.read().splitlines():
        liczba = int(l.split()[0])
        if liczba % 2 == 0:
            pierwsze = pierwsza(liczba)
            for p in pierwsze:
                if pierwsze[-1] + p == liczba or pierwsze[-2] + p == liczba:
                    print(liczba, p, liczba - p)
                    break
#           licznik += 1
# print("licznik: ", licznik)
