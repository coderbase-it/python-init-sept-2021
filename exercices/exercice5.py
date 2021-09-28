"""
Exercice5

Il faut créer un programme qui affiche les 20 premier terme de la table de multiplication de  7

Bonus : Pouvoir rendre variable le nombre de terme et la table choisie

Utiliser des functions
"""

import sys

print(sys.argv)
# ['D:/python-initiation-septembre-2021/exercices/exercice5.py', '40', '8']
nombre_termes = 20
table = 7

if len(sys.argv) > 1:
    nombre_termes = int(sys.argv[1])
if len(sys.argv) > 2:
    table = int(sys.argv[2])



def generate_multiplication_table(nombre_termes: int, table: int):
    for element in range(1, nombre_termes + 1):
        print(f"{table} X {element} = {table*element}")

generate_multiplication_table(nombre_termes=nombre_termes, table=table)
