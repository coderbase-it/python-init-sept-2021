# ouvrir / lire / écrire
# écrire du text ou du binaire

# 3 mode d'ouverture ( w écriture, a ajout ,
# r pour la lecture seule )
#


fichier = open('mon_fichier.txt', "w")
fichier.write('Bonjour')
fruits = ['banane', 'kiwi']
fichier.writelines(fruits)
fichier.close()
# Tout ce qui s'ouvre se ferme
# Créer le fichier si inexistant
# et supprime son contenu si existant
fichier = open('mon_fichier.txt', "a")
fichier.write('Hello')
fichier.close()
# Créer le fichier si inexistant
# et se positionne a la fin pour ajouter

# mode par default ( r )
fichier = open('mon_fichier.txt', "r")
print(fichier.read())
fichier.seek(0)
print(fichier.read(2))
print(fichier.readlines())
fichier.close()

with open('mon_fichier.txt', "a") as fichier:
    fichier.write('Fin programme')
    # pas besoin de fermer le fichier

print('Fin du programme on sait que le fichier est fermé')

# petit exemple lecture + écriture fichier
with open('mon_fichier.txt') as fichier:
    contenu = fichier.read()

print(contenu)
contenu *=2
with open('mon_fichier.txt', "w") as fichier:
    fichier.write(contenu)