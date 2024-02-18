with open("dane4.txt", "r") as f:
    t = f.read().splitlines()


tmp = []
maximum = []
roznica_tmp = 0
krotnosc_roznic = {}
for l in range(0, len(t) - 1):
    roznica = abs(int(t[l]) - int(t[l + 1]))
    if roznica in krotnosc_roznic:
        krotnosc_roznic[roznica] += 1
    else:
        krotnosc_roznic[roznica] = 1
    if not tmp:
        tmp.extend([t[l], t[l + 1]])
        roznica_tmp = roznica
    elif roznica_tmp == roznica:
        tmp.append(t[l + 1])
    else:
        tmp.clear()
        roznica_tmp = 0
    if len(tmp) > len(maximum):
        maximum = tmp.copy()

max_krotnosc = max(krotnosc_roznic.values())
# for k, v in krotnosc_roznic.items():
#     if v == max_krotnosc:
#         print(k)
print(f"zad 4.2: {len(maximum)}, początek: {maximum[0]}, koniec: {maximum[-1]}")  # rozw zad 4.2

print(f"max krotność: {max_krotnosc}, dla wartości: {[k for k, v in krotnosc_roznic.items() if v == max_krotnosc]}")
print(max(krotnosc_roznic, key=krotnosc_roznic.get))

# k_luk = {}
#
# with open('dane4.txt', 'r') as f:
#     seq = f.read().splitlines()
#
# for i in range(0, len(seq) - 1):
#     luka = abs(int(seq[i]) - int(seq[i+1]))
#     if luka in k_luk:
#         k_luk[luka] += 1
#     else:
#         k_luk[luka] = 1
#
# max_k = max(k_luk.values())
#
# print(max_k)
