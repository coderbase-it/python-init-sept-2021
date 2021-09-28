mon_dict = {
    "prenom": "Pierre",
    "nickname": "Pierrot",
    "names": ("Nédélec", "Troubat"),
    "age": 33
}

print(mon_dict, type(mon_dict))

# accès à un élèment
print(mon_dict["age"])

print(mon_dict.get("ages", "Pas trouvé"))

mon_dict["prenom"] = "Jean"

print(mon_dict)

# présence d'une clé
if 'prenom' in mon_dict:
    print('oui')

# présence d'une valeur
if 'prenom' in mon_dict.values():
    print('oui')

print(mon_dict.items())
# présence d'une valeur
if ('prenom', 'Jean') in mon_dict.items():
    print('oui')

for key, value in mon_dict.items():
    print(key, value)

# copy
import copy

a = mon_dict  # copie par référence
b = mon_dict.copy()  # copie par valeur de surface
c = copy.deepcopy(mon_dict)  # copie par valeur profonde

le_dict = {
    "user1": {
        "name": "Pierre",
        "age": 36
    },
    "user2": {}
}

print(le_dict['user1']['name'])
print(le_dict.get('user1').get('name'))

def ma_function(*args, lieu: str , **kwargs):
    print(args, lieu , kwargs )
    print(f"ma region est {kwargs.get('region')}")

ma_liste = [1 , 2 , 3]
ma_liste2 = [4,5,6]
ville = "Rennes"
ma_ville = {
    "region": "Bretagne",
    "country": "France",

}
ma_ville2 = {
    "region": "Bretagne",
    "country": "France",
    "lieu": "Maison"
}
ma_function(*ma_liste, *ma_liste2, lieu=ville, region="Bretagne",
            country ="France")

ma_function(*ma_liste, *ma_liste2, lieu=ville, **ma_ville)
ma_function(*ma_liste, *ma_liste2,  **ma_ville2)

my_age = 30
l = {
    "age": my_age
}

my_age += 1
print(l)
l['age'] = my_age