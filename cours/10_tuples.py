# un tuple est un itérable ( une liste immuable )

# un tuple vide
my_tuple = () # tuple()
print(my_tuple, type(my_tuple))

# un tuple avec un élèment
my_tuple = 99,# (99,)
print(my_tuple, type(my_tuple))

# un tuple avec plusieurs élèment
my_tuple = 99, 98 # (99,98)
print(my_tuple, type(my_tuple))

def my_function():
    return "Pierre", "Nédélec"

print(type(my_function()))
prenom , nom = my_function() # "Pierre", "Nédélec"
print(prenom, nom)

# passer d'un tuple a une liste et inversement
my_liste = [1 , 2 , 3]
print(tuple(my_liste))

my_tuple =  (1,2,3)
print(list(my_tuple))

# ne pas modifier/ ni ajouter les élèments d'un tuple
#my_tuple[0]= 99
import copy
my_tuple2 = copy.deepcopy(my_tuple)
print(id(my_tuple), id(my_tuple2))
my_tuple2 = (1,2,3,(4,6))
print(my_tuple2[3][1])
