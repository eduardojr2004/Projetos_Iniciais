nota = float(input("Informa a nota do aluno(a) entre 0 e 10: "))
if nota > 10 or nota < 0:
    print("Nota inválida!")
elif nota >= 9:
    nota_usa = "A"
elif nota >= 8:
    nota_usa = "B"
elif nota >= 7:
    nota_usa = "C"
elif nota >= 6:
    nota_usa = "D"
else:
    nota_usa = "E"
print(f"A sua nota no padrão EUA é: {nota_usa}")