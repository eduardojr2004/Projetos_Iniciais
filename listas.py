# CRIA UMA LISTA
notas = [7.8, 8.2, 9.5]

# ADICIONA UM NOVO VALOR A LISTA(9.9)
notas.append(9.9)

# ESCREVE OS VALORES DA LISTA / O TIPO DA LISTA  / O TIPO DO VALOR NA POSICAO 1 / VALOR NA POSICAO 1
print(f"A lista é: {notas}, o tipo da lista é: {type(notas)}, o tipo da posição [1] é: {type(notas[1])}, o valor na posição [1] é: {notas[1]}")

# ALTERAR VALOR DA POSICAO [2]
notas[2] = 9
print(notas, type(notas), type(notas[2]), notas[2])

# CONSULTAR ULTIMO VALOR DA LISTA
print(notas[-1])