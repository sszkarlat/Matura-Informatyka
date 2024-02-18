with open("liczby.txt", "r") as file:
    liczby = file.read().splitlines()

licznik = 0
licznik_2 = 0
licznik_8 = 0
dziesietne = []
with open("wynik4.txt", "w") as f:
    for liczba in liczby:
        if liczba.count("0") > liczba.count("1"):
            licznik += 1
    f.write("4.1: licznik-> " + str(licznik) + "\n")

    for liczba in liczby:
        if liczba[-1] == "0":
            licznik_2 += 1
        if liczba[-3::1] == "000":
            licznik_8 += 1
    f.write("4.2: licznik_2-> " + str(licznik_2) + " licznik_8-> " + str(licznik_8) + "\n")

    for liczba in liczby:
        dziesietne.append(int(liczba,2))

    f.write("4.3: min-> " + str(dziesietne.index(min(dziesietne))+1) + " max-> " + str(dziesietne.index(max(dziesietne))+1))


