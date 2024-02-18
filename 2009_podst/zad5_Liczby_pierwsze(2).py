from math import sqrt


def is_prime(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True


with open("liczby.txt", "r") as f:
    t = f.read().splitlines()

print("1 rozwiązanie:")
for l in t:
    if sqrt(int(l)) % 1 == 0 and is_prime(int(sqrt(int(l)))):
        print(l)
print("\n""2 rozwiązanie:")
for l in t:
    if int(l) ** 0.5 % 1 == 0 and is_prime(int(int(l) ** 0.5)):
        print(l)
print("\n""3 rozwiązanie:")
k = []
for l in range(1000):
    if is_prime(l):
        k.append(str(l ** 2))

for i in t:
    if i in k:
        print(i)
