import os
import shutil

# copier une fichier dans un dossier
src = os.path.join(os.getcwd(), 'test.txt')
dst = os.path.join(os.getcwd(), 'data' ,'test.txt')
shutil.copy(src, dst)

# copier + renommer une fichier dans un dossier
src = os.path.join(os.getcwd(), 'test.txt')
dst = os.path.join(os.getcwd(), 'data' ,'test2.txt')
shutil.copy(src, dst)

# Attention si le fichier dans le dossier destination
# existe déja il sera écrasé

# faire un backup d'un dossier ( récursif )
src = os.path.join(os.getcwd(), 'data' )
dst = os.path.join(os.getcwd(), 'data_backup' )
#shutil.copytree(src, dst )

# suppresion récursive
#shutil.rmtree(dst)

# déplacer ( + renommer )
src = os.path.join(os.getcwd(), 'test.txt' )
dst = os.path.join(os.getcwd(), 'data', )
shutil.move(src, dst)

# attention si le dossier de destination n'existe pas
# alors python créera un fichier portant le nom de ce dossier