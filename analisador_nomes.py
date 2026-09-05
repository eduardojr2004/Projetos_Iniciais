nome = input("Informe o nome: ")

print(f"O nome em letras MAIÚSCULAS é: {nome.upper()}")
print(f"O nome em letras MINÚSCULAS é: {nome.lower()}")

nome = nome.replace(" ","")
qtd_letras = len(nome)

print(f"A quantidade de letras é: {qtd_letras}")