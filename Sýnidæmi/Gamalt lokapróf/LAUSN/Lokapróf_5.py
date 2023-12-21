
orðabók = {}

with open("JorgeLuisBorgesQuote.txt", "r") as skrá_1:
    for lína in skrá_1:
        snyrt_lína = lína.replace(",", "").replace(".", "").split()
        for orð in snyrt_lína:
            if orð in orðabók:
                orðabók[orð] += 1
            else:
                orðabók[orð] = 1

heildarfjöldi_orða = sum(orðabók.values())
fjöldi_ólíkra_orða = len(orðabók)

print("Heildarfjöldi orða er: ", heildarfjöldi_orða)
print("Fjöldi ólíkra orða er: ", fjöldi_ólíkra_orða)