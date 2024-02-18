t = []

with open("dane.txt") as f:
    for l in f.read().splitlines():
        # t.append(list(map(int,l.split()))) --> trudniejsze rozwiazanie
        t.append(l.split())
najjasniejszy = 0
najciemniejszy = 255
for i in t:
    for j in i:
        if int(j) > najjasniejszy:
            najjasniejszy = int(j)
        elif int(j) < najciemniejszy:
            najciemniejszy = int(j)
print(f"najjasniejszy = {najjasniejszy}, najciemniejszy = {najciemniejszy}")
