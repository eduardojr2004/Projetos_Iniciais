nota = 0
alunos = [
#CHAVE : VALOR, CHAVE : VALOR
{"nome":"Ana","nota":8.5},
{"nome":"Maria","nota":5.5},
{"nome":"Pedro","nota":7.7},
{"nome":"João","nota":9.5},
]

for aluno in alunos:
    if aluno["nota"] >= 7:
        print(aluno["nome"])