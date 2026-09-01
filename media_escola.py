N1 = float(input("Informe a nota da primeira unidade."))
N2 = float(input("Informe a nota da segunda unidade."))
N3 = float(input("Informe a nota da terceira unidade."))
MEDIA = ((N1+N2+N3)/3)

if MEDIA >= 7:
    print(f"A media do Aluno(a) é: {MEDIA:.2f}, aprovado")
else:
    print(f"A media do Aluno(a) é: {MEDIA:.2f}, reprovado")