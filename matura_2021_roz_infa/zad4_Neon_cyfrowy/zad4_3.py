with open("instrukcje.txt") as f:
    t = []
    for l in f.read().splitlines():
        if "DOPISZ" in l:
            litera = l.split()[1]
            t.append(litera)
najczesciej = max(set(t), key=t.count)
print(najczesciej, t.count(najczesciej))
