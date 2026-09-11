cor = int(input("Escolha uma das cores:\n"
        "(1) BRANCA\n"
        "(2) VERMELHA\n"
        "(3) VERDE\n"
))

match cor:
        case 1:
            print("A cor escolhida é branca!")
            
        case 2:
            print("A cor escolhida é vermelha!")
            
        case 3:
            print("A cor escolhida é verde!")
            
        case _:
            print("Opção escolhida inválida!")