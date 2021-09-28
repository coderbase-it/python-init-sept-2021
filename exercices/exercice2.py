"""
Un programme qui demande à l"utilisateur de saisir des noms de chat
et le programme se stop une fois que l'utilisateur décide d'arrêter la saisie et
doit nous retourner la liste des chat saisie dans l'ordre de saisie
Bonus Exercice  : ne pas pouvoir saisir deux fois le même nom
de chat et afficher le numéro du chat à saisir ( example : saisir chat numéro 1 etc ... )
Votre programme doit gérer les exceptions de saisie
"""

liste_chat = []
reponse = ""
mot_stop = ["STOP", "stop"]
# Tant que la réponse n'est pas dans mot_stop
while reponse not in mot_stop:
    reponse = input(f"Entrez un unique nom de chat {len(liste_chat) + 1} ou STOP pour arreter: ")
    if reponse in mot_stop:
        break
    # strip enlève les espace dans la chaine reponse
    if reponse.strip() == '':
        # déclencher une exception
        raise ValueError('Attention pas de nom vide')
    if reponse not in liste_chat:
        liste_chat.append(reponse)
    else:
        print(f"Vous avez déjà mis le nom de chat {reponse}")


for index, nom_chat in enumerate(liste_chat):
    print(f"chat {index +1 } : {nom_chat}")
