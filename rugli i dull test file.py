

# a = '"sajdkasjdsak" "asdasdasds"' 

# a = a.replace('"', '')
# print (a)

# filename = "JorgeLuisBorgesQuote.txt"

# oll_ordin = []
# ord_talning = {}

# with open(filename, "r") as file:
#     raw_innihald = file.read().split()

# for ord in raw_innihald:
#     oll_ordin.append(ord.strip("“”,. ").lower())
# ("“”,. ")
# einstok_ord = set(oll_ordin)
# fjoldi_einstakra_orda = len(einstok_ord)
# heildarfjoldi_orda = len(oll_ordin)
# print (oll_ordin)
# print(f"Heildarfjöldi orða: {heildarfjoldi_orda}")
# print(f"Fjöldi einstakra orða: {fjoldi_einstakra_orda}")

def saekja_heiltolu(strengur):
    heiltala_komin = False
    while not heiltala_komin:
        try:
            tala = int(input(strengur))
            heiltala_komin = True
        except ValueError:
            print("Þetta skilst ekki sem heiltala, reyndu aftur...")
    return tala

PI = 3.14

input_komid = False
while not input_komid:
    try:
        radius = float(input("Sláðu inn radíus: "))
        input_komid = True
    except ValueError:
        print("Þetta var ekki heilbrigð tala hjá þér...")

val = 0
print("1. Flatarmál hrings")
print("2. Ummál hrings")
print("3. Rúmmál kúlu")
print("4. Hætta")
while val < 1 or val > 4:
    val = saekja_heiltolu("Veldu 1-4: ")

if(val == 1):
    flatarmal_hrings = radius*radius*PI
    print(f"Flatarmál hrings: {flatarmal_hrings}")
elif(val == 2):
    ummal_hrings = 2*radius*PI
    print(f"Ummál hrings: {ummal_hrings}")
elif(val == 3):
    rummal_kulu = (4.0*PI*(radius**3)) / 3.0
    print(f"Rúmmál kúlu: {rummal_kulu}")
#Dæmi 7
diction_words = {}
with open("HanSolo.txt", "r") as file:
    for line in file:
        new_line = line.lower().replace(",", "").replace(".", "").replace("?", "").split()
        for i in new_line:
            if i in diction_words:
                diction_words[i] += 1
            else:
                diction_words[i] = 1
            print (i)
summa = sum(diction_words.values())            
counter_above_1 = 0
for i in diction_words.values():
    if i > 1:
        counter_above_1 += 1
print (f"Orða sem koma oftar en einu sinni: {counter_above_1}")
print (f"total orð: {summa}")


