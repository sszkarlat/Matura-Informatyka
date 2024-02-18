t = []

with open("dane.txt") as f:
    for l in f.read().splitlines():
        t.append(l.split())

print(t[0][:160])
print(t[0][320:159:-1])
licznik = 0
for i in t:
    if not i[:160] == i[320:159:-1]:
        licznik += 1
print(licznik)
