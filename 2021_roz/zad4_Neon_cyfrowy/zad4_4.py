with open("instrukcje.txt") as f:
    t = []
    for l in f.read().splitlines():
        litera = l.split()[1]
        if "DOPISZ" in l:
            t.append(litera)
        elif "ZMIEN" in l:
            t[-1] = litera
        elif "USUN" in l:
            del t[-1]
        elif "PRZESUN" in l:
            if litera in t:
                if litera == "Z":
                    litera_p = "A"
                else:
                    litera_p = chr(ord(litera) + 1)
                index = t.index(litera)
                t[index] = litera_p
    print("".join(t))