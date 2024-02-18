# t = []
# p = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# with open("napisy.txt") as f:
#     for i in f.read().splitlines():
#         for l in i:
#             t.append(l)
# print(t)
# licznik = 0
# for l in t:
#     if l in p:
#         licznik += 1
# print(licznik)

licznik1 = 0
with open("napisy.txt") as f:
    wiersze = f.read().splitlines()
print(wiersze)
for wiersz in wiersze:
    for znak in wiersz:
        if znak.isnumeric():
            licznik1 += 1
print(licznik1)
