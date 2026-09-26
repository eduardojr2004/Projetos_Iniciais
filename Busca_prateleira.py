lista = ["Bolo", "Chocolate", "Laranja", "Farinha"]
cont = 0

for i in lista:
    if i == "Chocolate":
        break
    else:
        cont = cont + 1
print(f"O número de produtos até chegar nele foi: {cont + 1}")