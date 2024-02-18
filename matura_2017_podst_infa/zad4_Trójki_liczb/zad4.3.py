t = []
with open("liczby.txt", "r") as f:
    for l in f.readlines():
        t.append(l.split())


def suma(a):
    s = 0
    while a:  # dopóki zostały jakieś cyfry
        s += a % 10  # dodaj ostatnią cyfrę (jedności)
        a = a // 10  # podziel liczbę przez 10
    return s


suma_cyfr_wiersz = []
for i in range(len(t)):
    suma_cyfr_wiersz.append(suma(int(t[i][0])) + suma(int(t[i][1])) + suma(int(t[i][2])))

licznik_35 = 0
licznik_max = 0
max = 0
for i in range(len(suma_cyfr_wiersz)):
    tmp = suma_cyfr_wiersz[i]
    if suma_cyfr_wiersz[i] == 35:
        licznik_35 += 1
    if tmp > max:
        max = tmp
    else:
        tmp = 0
# for l in suma_cyfr_wiersz:
#     if l == max:
#         licznik_max += 1
print(f"liczba wystąpień 35: {licznik_35}, wartość maksymalna: {max}, "
      f"liczba wystąpień wartości maksymalnej: {suma_cyfr_wiersz.count(max)}")
