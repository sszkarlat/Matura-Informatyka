def is_prime(x):
    if x < 2:
        return False
    else:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True


t = []
with open("dane_przyklad.txt", "r") as f:
    for i in f.read().splitlines():
        if is_prime(int(i)):
            t.append(int(i))
    print(f"ilosc liczb pierwszych: {len(t)}\n"
          f"najwieksza liczba pierwsza: {max(t)}\n"
          f"najmniejsza liczba pierwsza: {min(t)}")




