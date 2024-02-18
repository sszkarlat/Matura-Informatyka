wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
with open("dane.txt") as f:
    for l in f.read().splitlines():
        suma = 0
        for i in range(len(wagi)):
            suma += wagi[i] * int(l[i])
        suma += int(l[-1])
        if suma % 10 != 0:
            print(l)
