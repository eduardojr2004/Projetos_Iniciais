lista = []

for i in range(5):
    item = input(f"Informe o {i+1}ª item: ")
    lista.append(item)
    
lista.remove(lista[1])
print(f"A lista de itens é:")
print(*lista, sep="\n")
print(f"O total de itens da lista é: {len(lista)}")