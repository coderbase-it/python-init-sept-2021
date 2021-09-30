# ensemble désordonné et sans doublon
avengers = {
    "hulk",
    "iron-man",
    "thanos"
}

print(avengers, type(avengers))
# ajouter un élément dans le set
avengers.add("ant-man")
avengers.add("ant-man")
avengers.add("ant-man")
print(avengers)
# ajouter de plusieurs élément
avengers.update(['captainAmerica', 'blackWidow'])

print(avengers)

# supprimer
avengers.remove('hulk')

for element in avengers:
    print(element)

if 'iron-man' in avengers:
    print('oui')

# conversion
ma_liste = [ 1 , 2 , 3 , 3 , 3 , 4 ]
myset= set(ma_liste)
print(myset)

myset.add(5)

my_new_list = list(myset)
print(my_new_list)