def silnia(n):
    if n == 0:
        return 1
    else:
        silnia = 1
        for i in range(1, n + 1):
            silnia *= i
        return silnia


# print(silnia(5))


with open("liczby.txt") as f:
    for l in f.read().splitlines():
        suma = 0
        for liczba in list(l):
            suma += silnia(int(liczba))
        if suma == int(l):
            print(l)
#
# with open("liczby.txt") as f:
#     for l in f.read().splitlines():
#         if sum([silnia(int(liczba)) for liczba in list(l)]) == int(l):
#             print(l)
