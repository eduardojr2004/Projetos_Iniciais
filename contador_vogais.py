nome = input("Informe a palavra ou frase: ")
nome = nome.lower()
cont = 0

for i in nome:
    if i in "aeiouáéíóúâêô":
        cont = cont + 1

print(f"O número de vogais é: {cont}")