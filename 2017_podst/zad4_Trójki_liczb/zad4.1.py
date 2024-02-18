t = []
with open("liczby.txt", "r") as f:
    for l in f.read().splitlines():
        t.append([int(i) for i in l.split()])
print(t)

licznik = 0
licznik2 = 0
for i in range(len(t)):
    if int(t[i][0]) < int(t[i][1]) < int(t[i][2]):
        licznik += 1
print(licznik)

for i in t:
    if i[0] < i[1] < i[2]:
        licznik2 += 1
print(licznik2)
