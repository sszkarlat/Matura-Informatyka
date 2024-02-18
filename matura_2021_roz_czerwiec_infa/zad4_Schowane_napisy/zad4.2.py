# t = []
#
# with open("napisy.txt") as f:
#     for i in f.read().splitlines():
#         for l in i:
#             t.append(l)
#
# s = []
# for x in range(950, len(t), 1001):
#     s.append(t[x])
# print("".join(s))

with open("przyklad.txt") as f:
    wiersze = f.read().splitlines()

t = wiersze[19::20]
print(t)
haslo = ""
kolumna = 0
for wiersz in t:
    haslo += wiersz[kolumna]
    kolumna += 1
print(haslo)
