opcao = "S"

while opcao.strip().upper() != "N":

    opcao_valida = True

    operacao = input("""
                    Escolha a operacao desejada:
                    Soma(+)
                    Subtração(-)
                    Multiplicação(*)
                    Divisão(/)
                    Digite a operação: """).strip()

    n1 = int(input("Informe o primeiro valor: "))
    n2 = int(input("Informe o segundo valor: "))

    match operacao:
        case "+":
            resultado = n1 + n2

        case "-":
            resultado = n1 - n2

        case "*":
            resultado = n1 * n2

        case "/":
            if n2 != 0:
                resultado = n1 / n2
            else:
                print("Não é possível dividir por zero")
                opcao_valida = False

        case _:
            print("Operação inválida!")
            opcao_valida = False

    if opcao_valida:
        print(f"O resultado da operação de {operacao} é: {resultado}")

    opcao = input("Deseja continuar? (S)im ou (N)ão: ").strip().upper()

print("Programa encerrado")