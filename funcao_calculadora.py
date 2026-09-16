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
(4) DIVISAO\n"""))

match opcao:
    case 1:
        calc = somar(n1,n2)
        nome_operacao = "somar"
        
    case 2:
        calc = subtrair(n1,n2)
        nome_operacao = "subtrair"

    case 3:
        calc = multiplicacao(n1,n2)
        nome_operacao = "multiplicacao"

    case 4:
        if n2 == 0:
            print("Não é possível dividir por zero")
        else:
            calc = divisao(n1,n2)
            nome_operacao = "divisao"

    case _:
        print("Operação inválida")

if opcao in (1,2,3) or (opcao == 4 and n2 != 0):
    print(f"O resultado da {nome_operacao} é: {calc}")