with open("analisador_arquivos.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

linhas_sem_quebra = [linha.rstrip("\n") for linha in linhas]

qtd_linhas = len(linhas_sem_quebra)

qtd_palavras = sum([len(linha.split()) for linha in linhas_sem_quebra])

maior_linha = max(linhas_sem_quebra, key=len)

print(f"Quantidade de linhas: {qtd_linhas}")
print(f"Quantidade de palavras: {qtd_palavras}")
print(f"Maior linha: {maior_linha}")

with open("analisador_arquivos_relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(f"Quantidade de linhas: {qtd_linhas}\n")
    arquivo.writelines(f"Quantidade de palavras: {qtd_palavras}\n")
    arquivo.writelines(f"Maior linha: {maior_linha}")