from typing import Tuple, Any


def ma_function(a : str, b: int) -> Tuple[str, str]:
    """
    Super function qui retourne a
    :param a:
    :param b:
    :return:
    """
    print(a, b)
    print('Hello')
    return a, 'Hello'


result = ma_function("Pierre",30)  # paramètre ordonné
result = ma_function(b=99, a="30")  # paramètre nommé
print(result)


# niveau 1 ( au plus simple )
def somme(a: int, b: int) -> int:
    return a + b

print(somme(1,2))
print(somme(1, somme(2 , 3)))

# niveau 2 ( additionner plusieurs nombres  ) en passant par une
# liste ( attention passage par référence , la function somme peut modifier la liste )
def somme(my_list) -> int:
    print(id(my_list))
    #my_list.append(10)
    acc = 0
    for element in my_list:
        acc +=element
    return acc

ma_liste = [1,2,3]
print(id(ma_liste))
print(somme(ma_liste))  # référence
print(ma_liste)

# niveau 3 ( passage de paramètre illimité à la function *args )
# passage par valeur grace à l'opérateur splat *
def sommefinal(*args):
    print(args)
    acc = 0
    for element in args:
        acc += element
    return acc

nombres = [ 3 , 4 , 5 , 6 ]
#sommefinal(nombres) # sommefinal([3 , 4 , 5 , 6])
sommefinal(*nombres, 99, 98)# sommefinal(3,4,5,6  , 99 , 98)




def ma_function(*args, lieu: str , sep: str = "-"):
    print(args, lieu , sep )

ma_liste = [1 , 2 , 3]
ma_liste2 = [4,5,6]
ville = "Rennes"

ma_function(*ma_liste, *ma_liste2, lieu=ville)

# function dans des functions
def ma_function():
    print('ma function')

    def lowercase(text:str):
        return text.lower()

    lowercase("Pierre")


# Variable Global
a = 9
print("Valeur de a avant la function", a )

def ma_function():
    global a
    a = 2
    print("Valeur de a dans la function", a)

ma_function()
print("Valeur de a après la function", a )



# functions anonymes lambda / function qui utilise d'autre functions
def double(a:int):
    return a *2

ma_liste = [ 1 , 2 , 3 , 4 ]

new_list = []
for element in ma_liste:
    new_list.append(double(element))
print(new_list)

# map permet d'appliquer une transformation à tous les élèments d'un itérable
mon_map= map(double, ma_liste)
print(list(mon_map))


mon_map= map(lambda x: x*2, ma_liste)
print(list(mon_map))

new_list = [ double(element) for element in ma_liste]

# filter
ma_liste = [ 6 , 7 , 8 , 9]
print(list(filter(lambda a: a % 2 == 0, ma_liste)))

