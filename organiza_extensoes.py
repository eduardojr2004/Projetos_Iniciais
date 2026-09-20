import os
import shutil

diretorio = r"E:\Meu Drive\Pessoal\Programacao\GitHub\Projetos_Iniciais\Diversos"

pasta_destino = {
    "imagens": os.path.join(diretorio, "Imagens"),
    "audios": os.path.join(diretorio, "Audios"),
    "documentos": os.path.join(diretorio, "Documentos"),
    "videos": os.path.join(diretorio, "Videos"),
    "outros": os.path.join(diretorio, "Outros"),
}

for pasta in pasta_destino:
    os.makedirs(pasta, exist_ok= True)


extensoes_imagens = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp"
}

# Extensões consideradas como áudios
extensoes_audios = {
    ".mp3",
    ".wav",
    ".ogg",
    ".m4a",
    ".wma",
    ".flac"
}

# Extensões consideradas como documentos
extensoes_documentos = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".csv"
}

# Extensões consideradas como vídeos
extensoes_videos = {
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".webm"
}


for arquivo in os.listdir(diretorio):

    caminho_arquivo = os.path.join(diretorio, arquivo)

    if not os.path.isfile(caminho_arquivo):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()

    if extensao in extensoes_imagens:
        destino = pasta_destino["imagens"]

    elif extensao in extensoes_audios:
        destino = pasta_destino["audios"]

    elif extensao in extensoes_documentos:
        destino = pasta_destino["documentos"]

    elif extensao in extensoes_videos:
        destino = pasta_destino["videos"]

    else:
        destino = pasta_destino["outros"]

shutil.move(caminho_arquivo, destino)