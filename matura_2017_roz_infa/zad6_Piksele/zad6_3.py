t = []

with open("dane.txt") as f:
    for l in f.read().splitlines():
        t.append(l.split())

licznik = 0

for i in range(200):
    for l in range(320):
        if l < 319 and abs(int(t[i][l]) - int(t[i][l + 1])) > 128:
            licznik += 1
        elif l > 0 and abs(int(t[i][l]) - int(t[i][l - 1])) > 128:
            licznik += 1
        elif i < 199 and abs(int(t[i][l]) - int(t[i + 1][l])) > 128:
            licznik += 1
        elif i > 0 and abs(int(t[i][l]) - int(t[i - 1][l])) > 128:
            licznik += 1
print(licznik)