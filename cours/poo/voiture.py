class Voiture:
    hasVolant = True
    nombre_roue = 4

    def __init__(self, couleur:str,  marque : str ):
        self.color = couleur
        self.brand = marque

    def klaxonner(self):
        print('Tchou Tchou')

    def repeindre(self, couleur:str):
        self.color = couleur

    def __str__(self):
        return f'Je suis une voiture {self.brand} de couleur {self.color}'

    def __eq__(self, other):
        return self.brand == other.brand

    def __gt__(self, other):
        return len(self.brand) > len(other.brand)

    def __lt__(self, other):
        return True

    def __len__(self):
        return len(self.color)

ma_voiture = Voiture("bleu", "Ford")
print(ma_voiture)
print(ma_voiture.color, ma_voiture.brand)
ma_voiture.repeindre('rouge')
print(ma_voiture)
print(f"Hello {ma_voiture}")
ma_voiture2 = Voiture('Noire', 'Bmw')
print(ma_voiture == ma_voiture2)
ma_voiture.__eq__(ma_voiture2)

print(ma_voiture > ma_voiture2)
print(len(ma_voiture2))

print(ma_voiture.__dir__())
print(ma_voiture.__dict__)