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

for element in os.scandir():
    print(element.name, element.path, element.is_dir(), element.is_file())
    if element.is_file():
        _, extension = os.path.splitext(element.name)
        for key, values in folder_dict.items():
            if extension.strip().lower() in values:
                chemin_dossier = os.path.join(os.getcwd(), key)
                os.makedirs(chemin_dossier, exist_ok=True)
                shutil.move(element.path, chemin_dossier)
