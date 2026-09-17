lista = []

for i in range(3):
    nome = input(f"Informe o nome do {i + 1}º produto: ")
    lista.append(nome)

#O i RECEBE A POSICAO E NOME RECEBE O NOME DA LISTA
for i, nome in enumerate(lista):
    print(i, nome)