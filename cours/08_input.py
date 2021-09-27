print("Veuillez saisir un nombre")

saisie = input()  # !! retourne uniquement des str
print(saisie, type(saisie))

# try:
#     # caster en  int
#     my_number = int(saisie)
# except ValueError as e:
#     print('traiter exception', e)
# else:
#     print(5 * my_number)
# finally:
#     print('fin du try finally')

while True:
    print("Veuillez saisir un nombre")

    saisie = input()  # !! retourne uniquement des str
    try:
        # caster en  int
        my_number = int(saisie)
    except ValueError as e:
        print('recommencez')
        continue

