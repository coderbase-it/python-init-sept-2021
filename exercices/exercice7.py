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