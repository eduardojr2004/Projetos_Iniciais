lista = []

for i in range(5):
    numero = int(input(f"Informe o {i + 1}ª número: "))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)

    else:
        cont = 0
        while cont < len(lista):
            if numero < lista[cont]:
                lista.insert(cont, numero)
                break
            cont += 1
print(f"Os valores da lista ordenados são: {lista}")