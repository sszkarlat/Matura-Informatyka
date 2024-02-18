t = []
with open("punkty.txt", "r") as f:
    for l in f.read().splitlines():
        t.append((int(l.split()[0]), int(l.split()[1])))

ilosc_punktow = 0
trafienie = 0

for l in range(len(t)):
    ilosc_punktow += 1

    if (t[l][0] - 200) ** 2 + (t[l][1] - 200) ** 2 <= 200 ** 2:
        trafienie += 1

    if ilosc_punktow == 100:
        pi100 = (4 * trafienie) / ilosc_punktow
        print("dla 100 pi = %.4f" % pi100)
    elif ilosc_punktow == 1000:
        pi1000 = (4 * trafienie) / ilosc_punktow
        print("dla 1000 pi = %.4f" % pi1000)
    elif ilosc_punktow == 5000:
        pi5000 = (4 * trafienie) / ilosc_punktow
        print("dla 5000 pi = %.4f" % pi5000)

piAll = (4 * trafienie) / ilosc_punktow
print("dla wszystkich pi = %.4f" % piAll)
