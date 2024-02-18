t = []
with open("punkty.txt", "r") as f:
    for l in f.read().splitlines():
        t.append((int(l.split()[0]), int(l.split()[1])))

licznik = 0
for l in range(len(t)):
    if (t[l][0] - 200) ** 2 + (t[l][1] - 200) ** 2 == 200 ** 2:
        print(f"punkty na okregu: {t[l]}")
    elif (t[l][0] - 200) ** 2 + (t[l][1] - 200) ** 2 < 200 ** 2:
        licznik += 1
print(f"punkty w okregu: {licznik}")
