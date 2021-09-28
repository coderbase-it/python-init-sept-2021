# les listes ( élèments itérables)

ma_liste = []
ma_liste2 = list()
print(ma_liste, ma_liste2)
print(type(ma_liste), type(ma_liste2))

liste = ['cat', 'elephant', [10,20,30],'mouse']

print(liste[1])
print(liste[2][1])
print(liste[-2][-2])

# ajouter un élément
ma_liste = [1 , 2 , 3]
ma_liste.append(4)
print(ma_liste)
ma_liste.insert(0,-99)
print(ma_liste)
ma_liste.insert(0,-99)
print(ma_liste)
print(ma_liste.count(-99))
print(len(ma_liste))
# suppression par valeur
ma_liste.remove(-99) # premier occurence uniquement
print(ma_liste)
# suppression par index
del ma_liste[0]
print(ma_liste)

# gestion mémoire
a = [ 9,8,7,5,6,4]
b = [ a[2], a[5] ]
print(b)
a[2] = 99
print(b)

# copie une liste
# copie par référence
garage1 = ['Ferrari', 'Ford', 'Mazda']
garage2 = garage1
print(garage1, garage2)
print(id(garage1), id(garage2))
# change une voiture dans garage1
garage1[0] = "Volvo"
print(garage1, garage2)
# copie par valeurs
garage1 = ['Ferrari', 'Ford', 'Mazda']
garage2 = garage1.copy() # garage1[:]
print(garage1, garage2)
print(id(garage1), id(garage2))
# change une voiture dans garage1
garage1[0] = "Volvo"
print(garage1, garage2)

import copy
liste = ['cat', 'elephant', [10,20,30],'mouse']
liste1 = copy.deepcopy(liste)
liste[0]='dog'
liste[2][1]= 50
print(liste, liste1)
print(id(liste[2]), id(liste1[2]))

# test appartenance
if 4 in ma_liste:
    print('Youpi')

# for
for element in ma_liste:
    print(element)

# Trier les listes
ma_liste = [ 5 , 2 , 3.14 , -7 , 1]
ma_liste.sort()# order croissant / trie par ordre mathématique car nombre
print(ma_liste)

ma_liste = [ 5 , 2 , 3.14 , -7 , 1]
ma_liste.sort(reverse=True)# order décroissant / trie par ordre mathématique car nombre
print(ma_liste)

ma_liste = [ 5 , 2 , 3.14 , -7 , 1]
ma_liste.reverse() # inverse la liste
print(ma_liste)

# passer d'une liste à un string et inversement
ma_liste = [ 'oui', 'yes', 'ok']
print("/".join(ma_liste))# oui/yes/ok

# chemin inverse
ma_chaine = "oui:yes:ok"
print(ma_chaine.split(":")) # ['oui', 'yes', 'ok']