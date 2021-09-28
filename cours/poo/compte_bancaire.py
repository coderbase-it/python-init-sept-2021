"""
Définissez une classe CompteBancaire(), qui permette d’instancier des objets tels que compte1, compte2, etc.
Le constructeur de cette classe initialisera deux attributs d’instance nom et solde,
avec les valeurs par défaut ’Dupont’ et 1000.
Trois autres méthodes seront définies :
• depot(somme) permettra d’ajouter une certaine somme au solde ;
• retrait(somme) permettra de retirer une certaine somme du solde ;
• affiche() permettra d’afficher le nom du titulaire et le solde de son compte.
"""


class CompteBancaire():

    def __init__(self, nom = "Dupont" , solde = 1000):
        self.nom = nom
        self.solde = solde

    def affiche(self):
        print(f"""
        nom : {self.nom}
        solde: {self.solde} 
        """)

    def depot(self, somme:int):
        if somme > 0:
            self.solde +=  somme

    def retrait(self, somme:int):
        if self.solde >= somme:
            self.solde -= somme



compte1 = CompteBancaire(nom="Nédélec", solde=800)
compte1.affiche()
compte1.depot(350)
compte1.affiche()
assert compte1.solde == 1150
compte1.retrait(200)
compte1.affiche()
assert compte1.solde == 950
compte2 = CompteBancaire()
compte2.affiche()
compte2.retrait(1001)
assert compte2.solde == 1000
print("fin du programme", )