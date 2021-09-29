import os
import shutil
folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

"""
Vous devez construire un organisateur de fichier à partir de ce dictionnaire
le programme scannera un dossier dans lequel il y a quelque fichier ( txt, pdf , ect ...  a vous de choisir )
 et devra créer le dossier correspondant au clé du dictionnaire , si durant le scanne on trouve des fichiers possédant une extension présent dans les valeurs du dictionnaire 
il faudra déplacer ces fichiers dans le dossier crée
 Exemple : dans mon dossier il y  a 1 fichier .pdf , le programme doit crée le dossier PDF et déplacé le fichier dedans
 Autre example : dans mon dossier il y a 1 fichier .txt, le programme doit crée le dossier PLAINTEXT et déplacé le fichier dedans

"""