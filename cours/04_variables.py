# nom de variable utilise le snake_case
# TOUS alphabets SAUF - , @ , ! , ? , \ , /, #
# un nom de variable ne doit pas commencer par
# un chiffre entier



ma_boite = 42
ma_boite2 = ma_boite
print(ma_boite)
print(id(ma_boite), id(42))
print(id(ma_boite2))

ma_boite = 5
print(ma_boite, ma_boite2)
print(id(ma_boite), id(ma_boite2))
