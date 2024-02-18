import math

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
    if ilosc_punktow == 1000:
        pi1000 = (4 * trafienie) / ilosc_punktow
    elif ilosc_punktow == 1700:
        pi1700 = (4 * trafienie) / ilosc_punktow
        
epsilon = abs(math.pi - pi1000).__round__(4)
epsilon1 = abs(math.pi-pi1700).__round__(4)
print(f"e1000 = {epsilon}\ne1700 = {epsilon1}")
