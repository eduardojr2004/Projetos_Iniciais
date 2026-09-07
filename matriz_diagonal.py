linha = 3
coluna = 3
soma = 0

matriz = []

for i in range(linha):
    linha_atual = []

    for j in range(coluna):
        elemento = int(input(f"Informe o elemento da posicao {i + 1}{j + 1}: "))
        linha_atual.append(elemento)
    matriz.append(linha_atual)

for i in range(linha):
    soma = soma + matriz[i][i]
print(f"A soma da matriz diagonal é: {soma}")