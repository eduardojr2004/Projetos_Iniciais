def somar(n1,n2):
    return n1 + n2

def subtrair(n1,n2):
    return n1 - n2

def multiplicacao(n1,n2):
    return n1 * n2

def divisao(n1,n2):
    return n1 / n2

n1 = float(input("Informe o primeiro valor: "))
n2 = float(input("Informe o segundo valor: "))

opcao = int(input("""
Informe a opção desejada:
(1) SOMA
(2) SUBTRACAO
(3) MULTIPLICACAO
(4) DIVISAO"""))

match opcao:
    case 1:
        calc = somar(n1,n2)
        
    case 2:
        calc = subtrair(n1,n2)

    case 3:
        calc = multiplicacao(n1,n2)

    case 4:
        calc = divisao(n1,n2)

if opcao == 1:
    print(f"A operação de soma é: {calc}")

elif opcao == 2:
    print(f"A operação de subtracao é: {calc}")

elif opcao == 3:
    print(f"A operação de multiplicacao é: {calc}")

elif opcao == 4:
    print(f"A operação de divisao é: {calc}")

else:
    print("Operação inválida!")
    calc = None