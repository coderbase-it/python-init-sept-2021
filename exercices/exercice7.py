import os
structure = {
    "Musique": [
        "Rock",
        "Jazz",
        "Pop"
    ],
    "Documents": [
        "Factures",
        "Travail",
        "Maison"
    ],
    "Images": [
        "Vacances",
        "Famille"
    ],
    "Videos": [
        "Chat",
        "Facebook"
    ]
}
# Parcourir la structure ( dictionnaire ) on aura besoin des clé et des valeurs
# pour chaque clé de mon dictionnaire je dois créer un dossier correspondant
# et également pour chaque valeurs de mon dictionnaire je dois avec un dossier
# Documents/Travail
# Documents/Maison
# Documents/Factures
# Bonus il faut pouvoir relancer le script plusieurs sans bug
print(structure.items())
#os.chdir('..')
for key, values in structure.items():
    # chemin_folder = os.path.join(os.getcwd(), key)
    # os.makedirs(chemin_folder, exist_ok=True)
    for value in values:
        # changer de répertoire
        chemin_subfolder = os.path.join(os.getcwd(), key, value)
        print(chemin_subfolder)
        os.makedirs(chemin_subfolder, exist_ok=True)