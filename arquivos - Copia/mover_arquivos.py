import os
import shutil

origem = "arquivos"
destino22 = "arquivos\22"
destino23 = "arquivos\23"

arquivos = os.listdir("arquivos")

for arquivo in arquivos:
    if arquivo.endswith(".txt"):
        if "22" in arquivo:
            caminho_origem = os.path.join(origem, destino22)
            caminho_destino = os.path.join(destino22, origem)
            shutil.move(caminho_origem, caminho_destino)

            if "23" in arquivo:
                caminho_origem = os.path.join(origem, destino23)
                caminho_destino = os.path.join(destino23, origem)
                shutil.move(caminho_origem, caminho_destino)

print("Arquivos movidos com sucesso!")