t = []
with open("liczby.txt", "r") as f:
    for l in f.readlines():
        t.append(l.split())


def NWD(x, y):
    while (y):
        x, y = y, x % y
    return x


nwd_list = []
for i in range(len(t)):
    nwd = NWD(NWD(int(t[i][0]), int(t[i][1])), int(t[i][2]))
    print(f"NWD: {nwd}")
    nwd_list.append(nwd)
print("Suma NWD:", sum(nwd_list))
