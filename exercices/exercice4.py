"""
à partir de cette liste
maliste = ['Jean', 'Maximilien',
'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
Fourni un programme permettant de séparer dans deux listes distinctes les prénoms avec  6 caractères ou plus et ceux avec moins de 6
"""

maliste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']

liste_sup6 = []
liste_inf6 = []

for element in maliste:
    if len(element) >= 6:
        liste_sup6.append(element)
    else:
        liste_inf6.append(element)

print(f"Liste à 6 éléments ou plus : {liste_sup6}\nListe à moins de 6 éléments : {liste_inf6}")

# Correction améliorer en utilisant les compréhensions de liste
liste_sup6 = [element for element in maliste if len(element) > 6]
print(liste_sup6)

liste_avec_10_premier_nombre_pair_au_carre = [element ** 2 for element in range(0, 20) if element % 2 == 0]
print(liste_avec_10_premier_nombre_pair_au_carre)

# compréhension de liste avec le else
liste_avec_10_premier_nombre_pair_au_carre_et_le_double_des_nombre_impairs \
    = [element ** 2 if element % 2 == 0 else element * 2 for element in range(0, 20)]
print(liste_avec_10_premier_nombre_pair_au_carre_et_le_double_des_nombre_impairs)
