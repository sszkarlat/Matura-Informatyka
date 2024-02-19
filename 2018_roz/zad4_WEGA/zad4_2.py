with open("przyklad.txt") as f:
    slowa = f.read().splitlines()


ileLiterMaSlowo = {
    slowo: len(set(slowo))
    for slowo in slowa
}

najwiecejLiter = max(ileLiterMaSlowo.values())
for slowo in ileLiterMaSlowo:
    if ileLiterMaSlowo[slowo] == najwiecejLiter:
        print(slowo, ileLiterMaSlowo[slowo])
