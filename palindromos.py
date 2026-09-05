nome = input("Informe o nome: ")

nome = nome.lower().replace(" ","")
if nome == nome[::-1]:
    print("A palavra/frase é um palíndromo!")
else:
    print("A palavra/frase NÃO é um palíndromo!")