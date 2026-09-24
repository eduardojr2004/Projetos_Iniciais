import getpass


def combinacoes(p1,p2):
    if((p1 == "pedra" and p2 == "tesoura") or (p1 == "papel" and p2 == "pedra") or (p1 == "tesoura" and p2 == "papel")):

        return "vencedor", "perdedor"

    else:
        return "perdedor", "vencedor"


jogadas_validas = {"pedra", "papel", "tesoura"}


p1 = getpass.getpass("Jogador 1 informe sua opção: ").lower().strip()
p2 = getpass.getpass("Jogador 2 informe sua opção: ").lower().strip()


if p1 not in jogadas_validas or p2 not in jogadas_validas:
    print("Opções inválidas!")

elif p1 == p2:
    print("Empate!")

else:
    resultado_1, resultado_2 = combinacoes(p1, p2)

    print(
        f"O jogador 1 é o {resultado_1}\n"
        f"O jogador 2 é o {resultado_2}"
        )