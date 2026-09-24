frase = "Este é um exemplo de texto que vamos justificar usando nosso programa"

palavras = frase.split()
conjunto = []
parcial = []
tamanho_atual = 0
tamanho_maximo = 18

for palavra in palavras:
    espaco = 1 if parcial else 0
    tamanho_palavra = len(palavra) + espaco

    if tamanho_atual + tamanho_palavra <= tamanho_maximo:
        parcial.append(palavra)
        tamanho_atual += tamanho_palavra

    else: 
        conjunto.append(" ".join(parcial))
        parcial = [palavra]
        tamanho_atual = len(palavra)

if parcial:
    conjunto.append(" ".join(parcial))

for linha in conjunto:
    print(linha)