import math


def is_prime(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True


t = []
with open("liczby.txt", "r") as f:
    for l in f.read().splitlines():
        t.append(l)
u = []
for i in range(0, len(t)):
    if str(round((math.sqrt(int(t[i]))), 2))[-1] == "0":
        u.append(int((math.sqrt(int(t[i])))))
for i in range(0, len(u)):
    if is_prime(u[i]) is True:
        print(u[i] ** 2)
