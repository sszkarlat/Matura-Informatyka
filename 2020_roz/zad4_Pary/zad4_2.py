with open("Dane_PR2/pary.txt") as f:
    for l in f.read().splitlines():
        tmp = []
        max = []
        for i in l.split()[1]:
            if not tmp or i in tmp:
                tmp.append(i)
            else:
                tmp.clear()
                tmp.append(i)
            if len(tmp) > len(max):
                max = tmp.copy()

        print("".join(max), len(max))
