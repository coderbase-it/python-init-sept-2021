# Types primitifs ( int , float , str , bool )

# entier ( int )
a = 5
print(type(a), type(int('5')))
#  provoque execptions de conversion int("Pierre")

# float
a = 5.0
print(type(a), float(2))

# boolean ( bool ) True False
a = True
print(type(a), type(False), bool(0), bool(1), bool(99))
print(bool("Pierre"), bool(''))

# str
name = "Pierre"
print(type(name), str(99))

prenom = "Pierre"
nom = "Nédélec"
code_postal = 35510

ma_phrase = f"mon code postal est le {code_postal}"
print(ma_phrase)

print(ma_phrase + ma_phrase)  # str + str
print(ma_phrase * 2)  # str * 2

# Algèbre de Bool
# not and
print(False and True)
print(False and (True or True))
print(not 2 + 2 == 4 and (2 + 2 != 5 or 2 * 2 == 4))

# b est compris entre 5 et 10
b = 6
a = 5 < b < 10
print(a)



