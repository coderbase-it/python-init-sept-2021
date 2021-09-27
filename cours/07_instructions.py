# Regle d'or Indentation
# conditionelle
name = "Pierre"
age = 35

if name == "Julien":
    print('Hello')
    print('World')
elif age == 35:
    print('Youpi')
else:
    print("Else")

print('Fin du programme')

# Index et boucle
name = "Pierre!"
print(name[0])
print(len(name))
print(name[-1])
print(id(name), id(name[0]), id(name[1]) )
print(id(name[2]), id(name[-2]))

print(name[0:3]) # borne de droite élèment non inclus
print(name[:3]) # borne de droite élèment non inclus
print(name[1:])
name = "Pierre!"
print(name[-5: -3])

# Boucles
for caract in name:
    print(caract)


for index, element in enumerate(name):
    print(index, element)

for element in range(0,20, 5):
    print(element)

i = 0
while i < 10:
    if i !=8:
        print('hello')
        break # sort de la boucle
        continue # viens retester la condition du while ou passer au tour suivant pour le for
    print('World')
    i = i + 1

print('Fin du programme')