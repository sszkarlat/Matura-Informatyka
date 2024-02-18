def czy_potega(x):
    while x % 3 == 0:
        x = x / 3
    return True if x == 1 else False


# l = [9,27,4]
#
# for k in l:
#     if czy_potega(k):
#         print(k)

licznik = 0
with open("liczby.txt") as f:
    for l in f.read().splitlines():
        if czy_potega(int(l)):
            licznik += 1
print(licznik)
