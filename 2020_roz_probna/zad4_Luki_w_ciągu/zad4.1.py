t = []
with open("dane4.txt", "r") as f:
    for l in f.read().splitlines():
        t.append(int(l))

roznica_max = 0
roznica_min = 2 * 10 ** 9
for l in range(len(t) - 1):
    roznica_tmp = abs(t[l] - t[l + 1])
    if roznica_tmp > roznica_max:
        roznica_max = roznica_tmp
        roznica_tmp = 0
    elif roznica_tmp < roznica_min:
        roznica_min = roznica_tmp
        roznica_tmp = 0
print(f"największa luka: {roznica_max}\nnajmniejsza luka: {roznica_min}")
