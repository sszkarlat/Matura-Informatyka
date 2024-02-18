def NWD(x, y):
    while (y):
        x, y = y, x % y
    return x


ciag = []
tmp_ciag = []
nwd = None
with open("liczby.txt") as f:
    numbers = f.read().splitlines()

for i in range(len(numbers) - 1):
    if ciag:
        tmp_nwd = NWD(tmp_nwd, int(numbers[i + 1]))
    else:
        tmp_nwd = NWD(int(numbers[i]), int(numbers[i + 1]))
    if tmp_nwd > 1:
        if ciag:
            tmp_ciag.append(numbers[i + 1])
        else:
            tmp_ciag.extend([numbers[i], numbers[i + 1]])
        if len(tmp_ciag) > len(ciag):
            ciag = tmp_ciag.copy()
            nwd = tmp_nwd
    else:
        tmp_ciag.clear()
        tmp_nwd = NWD(int(numbers[i]), int(numbers[i + 1]))
        if tmp_nwd > 1:
            tmp_ciag.extend([numbers[i], numbers[i + 1]])

print(ciag)
print(ciag[0])
print(len(ciag))
print(nwd)
