slowa = []
with open("slowa.txt", "r") as f:
    for l in f.read().splitlines():
        slowa.append((l.split()[0], l.split()[1]))
slowa_A = []
wiersze = []
anagramy = []
for para_slow in slowa:
    slowo_1 = para_slow[0]
    slowo_2 = para_slow[1]
    litery_drugiego_slowa = []
    litery_pierwszego_slowa = []
    for znak in slowo_2:
        litery_drugiego_slowa.append(znak)
    for znak in slowo_1:
        litery_pierwszego_slowa.append(znak)
    if sorted(litery_pierwszego_slowa) == sorted(litery_drugiego_slowa):
        anagramy.append(para_slow)
    if para_slow[0] in para_slow[1]:
        wiersze.append(para_slow)
    for slowo in para_slow:
        if slowo[-1] == "A":
            slowa_A.append(slowo)
print("Zadanie 6.1")
print(f"Ilość słów kończących się na literę A: {len(slowa_A)}")

print("\n""Zadanie 6.2")
print(f"Ilość wierszy: {len(wiersze)}")

print("\n""Zadanie 6.3")
print(f"Ilość anagramów: {len(anagramy)}")
