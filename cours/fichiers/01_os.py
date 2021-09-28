import os

t = r"zefzelf \n"

# Ne pas faire en python
chemin = "D:\python-initiation-septembre-2021\cours\fichiers\test.txt"

# méthode créer un chemin avec os.path.join
chemin = os.path.join( os.getcwd() , 'test.txt')
print(chemin)

# current working directory == emplacement du fichier python qu'on execute
print(os.getcwd())

# vérifier la présence d'un fichier test.txt
print(os.path.isfile(chemin))

# changer programmatiquement le répertoire courant
chemin_data = os.path.join(os.getcwd(), 'data')
os.chdir(chemin_data)
print(os.getcwd())

# création d'un dossier
os.makedirs('Images', exist_ok=True)

# lancer des commmandes depuis le terminal à travers python
#code = os.system('mkdir test3')
#print(code)

# Suppresion de fichier
# os.unlink('test.txt')

# supprimer un dossier uniquement si celui est vide sinon OSError
#os.rmdir('test3')

# récupérer l'extension d'un fichier à partir de son nom
name, extension = os.path.splitext('fichier.py')
print(name, extension)


# Parcours des répertoires
# parcours pour les dossiers et fichier en surface ( qui n'est pas récursif )
print(os.listdir(os.getcwd())) # ['Images', 'monfichier.txt', 'test3']

# parcours récursif ( retour de tuple )
for folder, sub_folders , files   in os.walk(os.getcwd()):
    print(folder, sub_folders, files)

"""
D:\python-initiation-septembre-2021\cours\fichiers\data ['Images', 'test3'] ['monfichier.txt']
D:\python-initiation-septembre-2021\cours\fichiers\data\Images [] []
D:\python-initiation-septembre-2021\cours\fichiers\data\test3 [] ['t']
"""

# parcours non récursif qui retourne des objects de
# class DirEntry( is_file(), is_dir(), name, path )
for element in os.scandir(os.getcwd()):
    print(element)
    print(element.is_file())
    print(element.is_dir())



