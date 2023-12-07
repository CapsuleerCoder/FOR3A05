
# #Dæmi 1
# def radius_spurning(radius):
#     villa = "vitlaust slegið inn, kæri notandi vinsamlega notist við leiðbeiningar"
#     try:
#         print ("Veldu 0 til að fá flatarmál hrings með þennan radíus ")
#         print ("Veldu 1 til að fá ummál hrings með þennan radíus ")
#         svar = int(input("Veldu 2 til að fá rummál kúlu með þennan radíus "))
#         if svar == 0:
#             flatarmal = radius*radius*3.14
#             return flatarmal
#         if svar == 1:
#             ummal = 2*radius*3.14
#             return ummal
#         if svar == 2:
#             rummal = (4*3.14*(radius**3))/3
#             return rummal
#         if svar < 0 or svar > 2:
#             return villa
#     except ValueError or ValueError:
#         return villa
    
# radius = float(input("sláðu inn radíus: "))
# dæmi1 = radius_spurning(radius)
# print (dæmi1)

# #Dæmi 2
# print ("Nú ætlum við að prenta allar tölur á talnabili nema þær sem eru margfeldi af 4 eða 7")
# num1 = int(input("Veldu lægri heiltölu: "))
# num2 = int(input("Veldu stærri heiltölu: "))
# def talnabil(lower, higher):
#     for i in range(lower, higher+1):
#         if i % 4 == 0 or i % 7 == 0:
#             continue
#         else:
#             print (i)
#     return "leyniskilaboð, þú ert flottur eða flott"

# talnabil(num1, num2)

# #Dæmi 3
# print ("Við ætlum að slá inn streng og tölu, tökum síðustu 3 stafi af strengnum og margföldum hann tölu sinnum.")
# word = input("Vinsamelegast sláðu inn einhverja setningu eða orð: ")
# multiply = int(input("Vinsamlega sláðu inn heiltölu"))
# def last_string_multiply(string, number):
#     last_string = string[-3:]
#     new_string = last_string*number
#     return new_string

# dæmi3 = last_string_multiply(word, multiply)
# print (dæmi3)

# #Dæmi 4 heimskuleg lausn. 
# binary = 11101
# sum = 0
# if binary >= 10000:
#     binary -= 10000
#     sum += 16
# if binary >= 1000:
#     binary -= 1000
#     sum += 8
# if binary >= 100:
#     binary -= 100
#     sum += 4
# if binary >= 10:
#     binary -= 10
#     sum += 2
# if binary >= 1:
#     binary -= 1
#     sum += 1
# print (sum)
# # binary 11101 er 1=1, 100 = 4, 1000 = 8, 10000 = 16
# # önnur og einfaldari leið fyrir dæmi 4
# prof = int("11101", 2)
# print ("int aðferðin, ", prof)# 29
# reverse_test = bin(29)
# print ("bin aðferðin(mínus 0b), ", reverse_test)
#11101 er 29.
# Þetta sést á því að tölurnar tákna 1 eða 0 sinnum 2 í einhverju veldi, frá
# hægri
# byrja veldin á 0 og hækka svo um einn eftir því sem við færumst til
# vinstri.
# þannig að 11101 er í raun 1*2^0+0*2^1+1*2^2+1*2^3+1*2^4
# = 1+0+4+8+16 = 29



# #Dæmi 5 næ ekki að losna við " í textanum. 
# word_dict = {}
# word_book = []
# total_words = 0
# with open("JorgeLuisBorgesQuote.txt", "r") as jorge:
#     for line in jorge:
#         word_list = line.split()
#         print (word_list)
#         for word in word_list:
#             total_words += 1
#             stripped_word = word.strip("“”,. ").lower()
#             print (stripped_word)
#             word_dict[stripped_word] = 1

# different_words = len(word_dict)
# print (f"Það eru {total_words} orð í skránni, það eru {different_words} ólík orð í skránni")
# print (word_dict)

# #Dæmi 6
# einkunn_listi = []
# number_5_or_above = 0
# number_of_10s = 0
# number_einkunn = int(input("Sláðu inn hversu margar einkunnir: "))
# for i in range(number_einkunn):
#     einkunn_input = int(input("Sláðu inn einkunn: "))
#     einkunn_listi.append(einkunn_input)
# highest = einkunn_listi[0]
# lowest = einkunn_listi[0]
# for einkunn in einkunn_listi:
#     if einkunn > highest:
#         highest = einkunn
#     if einkunn < lowest: 
#         lowest = einkunn
#     if einkunn >= 5:
#         number_5_or_above += 1
#     if einkunn == 10:
#         number_of_10s += 1
# print (f"Hæsta einkunn var: {highest}, lægsta einkunn: {lowest}")
# print (f"5 eða hærri einkunnir voru: {number_5_or_above}, fjöldi 10 einkunna: {number_of_10s}")

#Dæmi 7
class Sivalning:
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

    def __str__(self):
        return f"Radíus er {self.radius}, hæð er {self.height}"
    
    def rummal(self):
        rummal = self.height*3.14*self.radius**2
        return rummal
    
def main():
    print ("Nú ætlum við að fíflast aðeins með sívalving ")
    val_radius = float(input("Veldu radíus: "))
    val_height  =float(input("Veldu hæð: "))
    val_sivalving = Sivalning(val_radius, val_height)
    print (f"helstu stærðir eru {val_sivalving}")
    print (f"rúmmal hans er {val_sivalving.rummal()}")
main()
