with open("analisador_arquivo.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

# Remove a quebra de linha do final de cada linha
linhas_sem_quebra = [linha.rstrip("\n") for linha in linhas]

quantidade_linhas = len(linhas_sem_quebra)

# Conta as palavras de todas as linhas
quantidade_palavras = sum(len(linha.split()) for linha in linhas_sem_quebra)

# Encontra a maior linha
if linhas_sem_quebra:
    maior_linha = max(linhas_sem_quebra, key=len)
else:
    maior_linha = ""

# Mostra os resultados na tela
print(f"Quantidade de linhas: {quantidade_linhas}")
print(f"Quantidade total de palavras: {quantidade_palavras}")
print(f"Maior linha: {maior_linha}")

# Salva os resultados no relatório
with open("analisador_arquivo_relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Quantidade de linhas: {quantidade_linhas}\n")
    arquivo.write(f"Quantidade total de palavras: {quantidade_palavras}\n")
    arquivo.write(f"Maior linha: {maior_linha}\n")