qtd_elementos = int(input("Informe o número de elementos da lista: "))

lista = []

for l in range(qtd_elementos):
    elemento = input(f"Informe o elemento de número: {l + 1}: ")
    lista.append(elemento)

print(*lista)