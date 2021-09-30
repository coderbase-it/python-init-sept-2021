from cours.poo.voiture import Voiture

def main():
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


if __name__ == "__main__":
    main()

