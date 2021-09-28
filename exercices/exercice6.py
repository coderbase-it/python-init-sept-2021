"""
écrire une programme qui me demande de saisir en anglais dans un premier temp ,
le nom d'un mois et le programme donne le nombre de jours de ce mois .
2ième partie , laissez la posibilité au joueur de saisi une mois en français également
Si l'utilisateur vous parle en francais lui répondre en francais
si l'utilisateur parle en anglais lui répondre en anglais
"""

# Un dictionnaire d'association nom de mois / jour
months = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}
# Un second dictionnaire d'association des noms de mois français / anglais
frTranslator = {
    "janvier": "january",
    "février": "february",
    "mars": "march",
    "avril": "april",
    "mai": "may",
    "juin": "june",
    "juillet": "july",
    "août": "august",
    "septembre": "september",
    "octobre": "october",
    "novembre": "november",
    "décembre": "december"
}
