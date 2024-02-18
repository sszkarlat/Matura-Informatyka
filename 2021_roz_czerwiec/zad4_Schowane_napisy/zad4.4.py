with open("napisy.txt") as f:
    wiersze = f.read().splitlines()

haslo = ""
for wiersz in wiersze:
    tmp = []
    for znak in wiersz:
        if znak.isnumeric():
            tmp.append(znak)
    for i in range(0, len(tmp) - 1, 2):
        liczba = int(tmp[i] + tmp[i + 1])
        if 65 <= liczba <= 90:
            haslo += chr(liczba)
    if haslo[-1:-4:-1] == "XXX":
        break
    # if "XXX" in haslo:
    #     break
print(haslo)

# t = [1,2,3,4,5,6,4,2,4] #- wtedy kiedy przechodze po zbiorze
#             # danych, w którym potrzebuje porownac wiele elementow
#             #kilka elementow na raz
# for liczba in range(0,len(t)-1):
#     if (t[liczba] + t[liczba+1]) % 2 == 0:
#         print("dobrze")
