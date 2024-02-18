def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


t = []
with open("dane4.txt", "r") as f:
    for l in f.read().splitlines():
        t.append(int(l))
pierwsze = []
for i in t:
    if is_prime(i):
        pierwsze.append(i)
print("ilość liczb:", len(pierwsze))

print(f"najmniejsza liczba: {min(pierwsze)}, największa liczba: {max(pierwsze)}")

licznik1 = 0
for l in range(0, len(t) - 1):
    if is_prime(t[l]) and is_prime(t[l + 1]) and abs(t[l] - t[l + 1]) == 2:
        licznik1 += 1
        print(t[l], t[l + 1])
print(licznik1, "pary")
