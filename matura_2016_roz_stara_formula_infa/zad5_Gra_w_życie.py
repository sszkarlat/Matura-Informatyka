import copy

plansza = []
zadanie5_1 = 0
cords = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
with open("gra.txt", "r") as f:
    for l in f.read().splitlines():
        plansza.append(list(l.rstrip()))

for l in range(2, 100):
    robocza = copy.deepcopy(plansza)
    for i in range(12):
        for j in range(20):
            znacznik = 0
            for k in cords:
                y = k[0] + j
                x = k[1] + i
                if x > 11:
                    x = 0
                elif x < 0:
                    x = 11
                if y > 19:
                    y = 0
                elif y < 0:
                    y = 19
                if plansza[x][y] == "X":
                    znacznik += 1
            if (i==1 and j==18 and l==38):
                zadanie5_1 = znacznik
            if (znacznik in (2,3) and plansza[i][j] == "X") or (znacznik == 3 and plansza[i][j] == "."):
                robocza[i][j] = "X"
            else:
                robocza[i][j] = "."
    plansza = copy.deepcopy(robocza)
print(zadanie5_1)
