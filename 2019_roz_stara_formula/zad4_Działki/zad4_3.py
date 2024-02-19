dzialki = []
dzialka = []
with open("przyklad.txt") as f:
    for i in f.read().splitlines():
        if i != "":
            dzialka.append(i)
        else:
            dzialki.append(dzialka)
            dzialka = []


przeszkodyWszystkie = []
przeszkody = []
for k in range(len(dzialki)):
    dzialka = dzialki[k]
    przeszkoda = (0, 0)
    flag = "false"
    index = 1
    if dzialka[i][i] == "X":
        przeszkoda = (i, j)
        flag = "true"
    else:
        i += 1
        print(i, j)
        index += 1
    przeszkodyWszystkie.append(przeszkody)
print(przeszkodyWszystkie)

# tmp = 0
# index = 0
# for i in range(len(przeszkodyWszystkie)):
#     if max(przeszkodyWszystkie[i]) > tmp:
#         tmp = max(przeszkodyWszystkie[i])
#         index = i + 1
# print(tmp, index)
