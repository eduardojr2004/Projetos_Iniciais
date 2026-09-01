linha = int(input("Informe o número de linhas da matriz: "))
coluna = int(input("Informe o número de colunas da matriz: "))

matriz = []

for l in range(linha):
    linha_atual = []
    for c in range(coluna):
        elemento = int(input(f"Informe o elemento {l + 1}{c + 1}: "))
        linha_atual.append(elemento) 
    matriz.append(linha_atual)

for linha in matriz:
    print(*linha)