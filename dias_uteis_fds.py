dia = int(input("Informe o dia da semana:\n"
                "(1)Domingo\n"
                "(2)Segunda\n"
                "(3)Terça\n"
                "(4)Quarta\n"
                "(5)Quinta\n"
                "(6)Sexta\n"
                "(7)Sábado\n"
))

match dia:
    case 1 | 7:
        print("Final de semana")

    case 2 | 3 | 4 | 5 | 6:
        print("Dia da semana")

    case _:
        print("Entrada inválida!")