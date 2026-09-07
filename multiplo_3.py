soma = 0

for i in range(1,500):
    if (i % 3 == 0 and i % 2 != 0):
        soma = soma + i
print(f"A soma dos números multiplos de 3 é: {soma}")