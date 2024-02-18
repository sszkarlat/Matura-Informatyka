from math import sqrt

with open("liczby.txt") as f:
    data = f.read().splitlines()

# print(data)

numbersList = []
for number in data:
    if number[0] == number[-1]:
        numbersList.append(number)


# print(len(numbersList), numbersList[0])

def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range(2, int(sqrt(number) + 1)):
            if number % i == 0:
                return False
        return True


listaLiczbPierwszych = [
    i
    for i in range(2, 100000)
    if is_prime(i) is True
]


# with open("liczbyPierwsze.txt", "w") as odp:
#     for i in listaLiczbPierwszych:
#         odp.write(str(i) + "\n")


# print(is_prime(2))


def rozklad_na_czynniki(number):
    listaCzynnikow = []
    while number > 1:
        for i in listaLiczbPierwszych:
            if number % i == 0:
                listaCzynnikow.append(i)
                number //= i
                break
    return listaCzynnikow


slownikRozkladuLiczb = {
    i: len(rozklad_na_czynniki(int(i)))
    for i in data
}

slownikRozkladuLiczbSet = {
    i: len(set(rozklad_na_czynniki(int(i))))
    for i in data
}

# for i in slownikRozkladuLiczb:
#     if slownikRozkladuLiczb[i] == max(slownikRozkladuLiczb.values()):
#         print(i, slownikRozkladuLiczb[i])

# for i in slownikRozkladuLiczbSet:
#     if slownikRozkladuLiczbSet[i] == max(slownikRozkladuLiczbSet.values()):
#         print(i, slownikRozkladuLiczbSet[i])


data2 = [
    int(i)
    for i in data
]

# print(data2)
counter1 = 0
with open("trojki.txt", "w") as trojki:
    for z in data2:
        for y in data2:
            if y % z == 0 and y != z:
                for x in data2:
                    if x % y == 0 and x != y:
                        trojki.write(str(z) + " ")
                        trojki.write(str(y) + " ")
                        trojki.write(str(x) + "\n")
                        counter1 += 1
# print("Trojki:", counter1)

counter2 = 0
for z in data2:
    for y in data2:
        if y % z == 0 and y != z:
            for x in data2:
                if x % y == 0 and x != y and x != y:
                    for w in data2:
                        if w % x == 0 and w != x:
                            for u in data2:
                                if u % w == 0 and w != u:
                                    # print(z, y, x, w, u)
                                    counter2 += 1

# print("Piatki:", counter2)
