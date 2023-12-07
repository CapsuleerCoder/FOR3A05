import string
orðabók = {}

with open("JorgeLuisBorgesQuote.txt", "r") as skrá_1:
    for lína in skrá_1:
        snyrt_lína = lína.split()
        for orð in snyrt_lína:
            nýtt_orð = orð.strip().strip(string.punctuation).lower()
            if nýtt_orð in orðabók:
                orðabók[nýtt_orð] += 1
            else:
                orðabók[nýtt_orð] = 1

heildarfjöldi_orða = sum(orðabók.values())
fjöldi_ólíkra_orða = len(orðabók)
print(orðabók)
print("Heildarfjöldi orða er: ", heildarfjöldi_orða)
print("Fjöldi ólíkra orða er: ", fjöldi_ólíkra_orða)

"""
heildarfjöldi_orða = 0
fjöldi_ólíkra_orða = 0

for key in orðabók:
    fjöldi_ólíkra_orða += 1
    heildarfjöldi_orða += orðabók[key]
"""






