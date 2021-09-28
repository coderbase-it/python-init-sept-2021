from cours.poo.voiture import Voiture


class VoitureDeCourse(Voiture ):

    def __init__(self, couleur, marque, speed):
        Voiture.__init__(self, couleur, marque)
        # super().__init__(couleur, marque)
        self.speed = speed

    def __str__(self):
        return f'Je suis une voiture {self.brand} ' \
               f'de couleur {self.color} ' \
               f'vitesse: {self.speed}'

    def parentPresenter(self):
        return super().__str__()

ma_ferrari = VoitureDeCourse('rouge', 'ferrari', 400)
print(ma_ferrari)
print(ma_ferrari.parentPresenter())
