with open("przyklad.txt") as f:
    slowa = f.read().splitlines()

przeslanie = ""
for i in range(39, len(slowa), 40):
    przeslanie += slowa[i][9]

print(przeslanie)
