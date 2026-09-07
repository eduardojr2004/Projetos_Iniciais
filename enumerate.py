lista = []

for i in range(3):
    nome = input(f"Informe o nome do {i + 1}º produto: ")
    lista.append(nome)

for i, nome in enumerate(lista):
    print(i, nome)