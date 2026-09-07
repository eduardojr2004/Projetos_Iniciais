lista = []
cont = 0
aux = 0

for i in range(5):
    nome = input(f"Informe o {i + 1}º nome: ")
    lista.append(nome)

while cont < 5:
    if cont == 0:
        print(f"O primeiro da fila é: {lista[aux]}")
        lista.pop(aux)
    elif (cont > 0 and cont < 5):
        print(f"O próximo(a) da fila é: {lista[aux]}")       
        lista.pop(aux)
    cont += 1
if cont == 5:
        print("Esse foi o último da fila!")