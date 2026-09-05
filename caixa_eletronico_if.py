valor = int(input("Informe o valor a ser sacado: "))

if valor < 0:
    print("Valor inválido!")
    
elif valor == 0:
    print("Nenhum valor a ser sacado.")
    
else:
    cinquenta = valor // 50
    restante = valor % 50

    vinte = restante // 20
    restante = restante % 20

    dez = restante // 10
    restante = restante % 10

    um = restante

    print(f"Serão sacadas {cinquenta} notas de R$ 50,00")
    print(f"Serão sacadas {vinte} notas de R$ 20,00")
    print(f"Serão sacadas {dez} notas de R$ 10,00")
    print(f"Serão sacadas {um} notas de R$ 1,00")