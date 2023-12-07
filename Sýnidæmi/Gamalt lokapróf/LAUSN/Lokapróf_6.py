
einkunnir = []
fjöldi_nemenda = int(input("Hversu margir voru nemendurnir ? "))

for i in range(fjöldi_nemenda):
    næsta_einkunn = int(input("Sláðu inn næstu einkunn."))
    einkunnir.append(næsta_einkunn)

hæsta_einkunn = einkunnir[0]
lægsta_einkunn = einkunnir[0]
fjöldi_5_eða_hærra = 0
fjöldi_10 = 0

for e in einkunnir:
    if e > hæsta_einkunn:
        hæsta_einkunn = e
    if e < lægsta_einkunn:
        lægsta_einkunn = e
    if e >= 5:
        fjöldi_5_eða_hærra += 1
    if e == 10:
        fjöldi_10 += 1

print("Hæsta einkunn er: ", hæsta_einkunn)
print("Lægsta einkunn er: ", lægsta_einkunn)
print("Fjöldi nemenda með 5 eða meir er: ", fjöldi_5_eða_hærra)
print("Fjöldi nemenda með 10 er: ", fjöldi_10)

