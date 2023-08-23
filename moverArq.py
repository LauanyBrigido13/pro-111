import os
import shutil

# Define os diretórios de origem e destino
from_dir = r"C:\Users\Leandro Miranda\Downloads\imagens-C114-main\imagens-C114-main"
to_dir = r"C:\Users\Leandro Miranda\Downloads\imagens2"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension =os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Arquivos_documentos"
        path3 = to_dir + '/' + "Arquivos_documentos"+ '/' +file_name

    if os.path.exists(path2):
        print("Movendo"+ file_name + " . . .")
        shutil.move(path1, path2)
    else:
        os.makedirs(path2)
        print("Movendo"+ file_name + " . . .")
        shutil.move(path1, path3)


