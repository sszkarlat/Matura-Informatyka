with open("instrukcje.txt") as f:
    t_max = []
    tmp = []
    for l in f.read().splitlines():
        instrukcja = l.split()[0]
        if not tmp:
            tmp.append(instrukcja)
        elif instrukcja in tmp:
            tmp.append(instrukcja)
            if len(tmp) > len(t_max):
                t_max = tmp.copy()
        else:
            tmp.clear()
            tmp.append(instrukcja)
    print(f"rodzaj instrukcji - {t_max[0]}, długość ciągu - {len(t_max)}")
