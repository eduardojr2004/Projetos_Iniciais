import os
import shutil

origem = r"E:\Meu Drive\Pessoal\Programacao\GitHub\Projetos_Iniciais\arquivos"
destino22 = os.path.join(origem, "22")
destino23 = os.path.join(origem, "23")

arquivos = os.listdir(origem)

for arquivo in arquivos:
    if arquivo.endswith(".txt"):
        caminho_origem = os.path.join(origem, arquivo)

        if "22" in arquivo:
            shutil.move(caminho_origem, destino22)

        elif "23" in arquivo:
            shutil.move(caminho_origem, destino23)

print("Arquivos movidos com sucesso!")