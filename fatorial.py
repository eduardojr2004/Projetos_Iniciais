numero = int(4)
lista = []
resultado = 1
while numero > 0:
    lista.append(numero)
    numero = numero - 1
for n in lista:
    resultado *= n
print(resultado)