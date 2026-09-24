frase = input("Informe a frase: ").lower().strip()
antiga = input("Informe a palavra que quer substituir: ").lower().strip()
nova = input("Informe a palavra que deseja inserir: ").lower().strip()
nova_frase = []

palavras = frase.split()

for palavra in palavras:
    if palavra == antiga:
        nova_frase.append(nova)

    else:
        nova_frase.append(palavra)

frase_final = " ".join(nova_frase)
print(frase_final)