with open("mecz.txt") as f:
    data = f.read().strip()

# print(data)

counter = 0
for i in range(len(data) - 1):
    if data[i + 1] != data[i]:
        counter += 1

# print(counter)

counterA = 0
counterB = 0
# for i in data:
#     if (counterA >= 1000 or counterB >= 1000) and (abs(counterA - counterB) >= 3):
#         if counterA > counterB:
#             print(f"A {counterA}:{counterB}")
#         else:
#             print(f"B {counterA}:{counterB}")
#         break
#     else:
#         if i == "A":
#             counterA += 1
#         else:
#             counterB += 1

# dane = "BBBBBBBBBBAABBAAAAAAAAAAABA"

counter = 1
passa = []
ListaPass = []
for i in range(len(data) - 1):
    if not passa:
        passa.append(data[i])
    if data[i] == data[i + 1]:
        passa.append(data[i + 1])
    else:
        if len(passa) >= 10:
            ListaPass.append(passa)
            passa = []
        else:
            passa = []

listaDlugosci = {
    ListaPass[i][0]: len(ListaPass[i])
    for i in range(len(ListaPass))
}

print(listaDlugosci)
print(len(listaDlugosci), end=" ")
for i in listaDlugosci:
    if listaDlugosci[i] == max(listaDlugosci.values()):
        print(i, listaDlugosci[i])
        break
