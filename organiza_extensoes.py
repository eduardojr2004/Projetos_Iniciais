import os
import shutil

caminho = r"E:\Meu Drive\Pessoal\Programacao\GitHub\Projetos_Iniciais\Diversos"


extensoes_imagens = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".webp"
)

# Extensões consideradas como áudios
extensoes_audios = (
    ".mp3",
    ".wav",
    ".ogg",
    ".m4a",
    ".wma",
    ".flac"
)

# Extensões consideradas como documentos
extensoes_documentos = (
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".csv"
)

# Extensões consideradas como vídeos
extensoes_videos = (
    ".mp4",
    ".avi",
    ".mkv",
    ".mov",
    ".wmv",
    ".webm"
)

#CAMINHO DAS PASTAS
diretorios_arquivos = {
    "DIR_IMAGENS": os.path.join(caminho,"Imagens"),
    "DIR_AUDIOS" : os.path.join(caminho, "Audios"),
    "DIR_DOCUMENTOS" : os.path.join(caminho, "Documentos"),
    "DIR_VIDEOS" : os.path.join(caminho, "Vídeos"),
    "DIR_OUTROS" : os.path.join(caminho, "Outros")
}

#VERIFICA SE AS PASTAS EXISTEM, SE NÃO EXISTIR CRIA
for diretorio in diretorios_arquivos.values():
    if not os.path.isdir(diretorio):
        os.makedirs(diretorio, exist_ok=True)


#ARQUIVOS RECEBE TODO CONTEÚDO DO CAMINHO
arquivos = os.listdir(caminho)


#RECEBE E ANALISA CADA ITEM DO CAMINHO
for arquivo in arquivos:

    local_arquivo = os.path.join(caminho, arquivo)

    if os.path.isdir(local_arquivo):
        continue

    # Converte o nome do arquivo para letras minúsculas
    # Isso permite reconhecer arquivos como FOTO.JPG ou musica.MP3
    nome_arquivo = arquivo.lower()        

    if nome_arquivo.endswith(extensoes_imagens):
        destino = diretorios_arquivos["DIR_IMAGENS"]

    elif nome_arquivo.endswith(extensoes_audios):
        destino = diretorios_arquivos["DIR_AUDIOS"]

    elif nome_arquivo.endswith(extensoes_documentos):
        destino = diretorios_arquivos["DIR_DOCUMENTOS"]

    elif nome_arquivo.endswith(extensoes_videos):
        destino = diretorios_arquivos["DIR_VIDEOS"]

    else:
        destino = diretorios_arquivos["DIR_OUTROS"]

    shutil.move(local_arquivo, destino)

print("Arquivo(s) movidos!")