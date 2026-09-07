lista = []
soma = 0

for i in range(5):
    numero = int(input(f"Informe o {i + 1} número inteiro: "))
    lista.append(numero)
    soma += numero

    if i == 0:
        maior = lista[i]
        menor = lista[i]

    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero

print(f"A soma dos números é: {soma}")
print(f"A media dos número é: {soma/len(lista)}")
print(f"O MENOR valor é: {menor}")
print(f"O MAIOR valor é: {maior}")