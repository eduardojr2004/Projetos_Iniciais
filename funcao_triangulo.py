def funcao_triangulo(L1,L2,L3):
    return((L1 + L2) > L3) and ((L1 + L3) > L2) and ((L2 + L3) > L1)

L1 = float(input("Informe o primeiro lado: "))
L2 = float(input("Informe o segundo lado: "))
L3 = float(input("Informe o terceiro lado: "))

if funcao_triangulo(L1,L2,L3):
    print("É triângulo")
else:
    print("Não é um triângulo")