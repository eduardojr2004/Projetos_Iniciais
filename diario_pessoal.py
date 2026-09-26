lista_frases = []

for i in range(3):
    frase = input(f"Informe a {i + 1}° frase: ")
    lista_frases.append(frase + "\n")

with open("lista_diario.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(lista_frases)

with open("lista_diario.txt", "r", encoding="utf-8") as arquivo:
    leitura = arquivo.readlines()
    for i in leitura:
        print(i,end="")