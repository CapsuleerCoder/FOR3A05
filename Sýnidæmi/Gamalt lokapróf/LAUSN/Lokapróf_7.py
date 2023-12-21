
class Sívalningur:
    # smiður
    def __init__(self, radíus, hæð):
        self.radíus = radíus
        self.hæð = hæð
    
    # strengjaútgáfa svo hægt sé að prenta út tilvik af klasanum
    def __str__(self):
        return "Radíus: {}, Hæð: {}".format(self.radíus, self.hæð)
    
    def rúmmál(self):
        return self.hæð*3.14*self.radíus**2
    

def main():
    radíus = float(input("Sláðu inn radíus sívalnings. "))
    hæð = float(input("Sláðu inn hæð sívalnings. "))
    sívalningurinn_okkar = Sívalningur(radíus, hæð)
    print("Rúmmál sívalningsins er: ", sívalningurinn_okkar.rúmmál())
    print("Helstu stærðir sívalningsins eru: ", sívalningurinn_okkar)

main()

