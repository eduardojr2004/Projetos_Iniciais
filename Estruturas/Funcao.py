# Função que calcula a média de três notas
def calcular_media(nota1, nota2, nota3):
    # Soma as três notas
    soma = nota1 + nota2 + nota3

    # Divide a soma pela quantidade de notas
    media = soma / 3

    # Devolve o resultado da média
    return media


# --------------------------------------------------
# Exemplos de manipulação da função
# --------------------------------------------------

# 1. Chamando a função com três valores
media_aluno1 = calcular_media(8, 7, 9)

# Resultado: 8.0
print(media_aluno1)


# 2. Chamando a função com outros valores
media_aluno2 = calcular_media(10, 9, 8)

# Resultado: 9.0
print(media_aluno2)


# 3. Exibindo uma mensagem junto com o resultado
media_aluno3 = calcular_media(6, 7, 5)

# Resultado: A média do aluno é: 6.0
print("A média do aluno é:", media_aluno3)


# 4. Armazenando o resultado em uma variável
resultado = calcular_media(4, 5, 6)

# Resultado: 5.0
print("Resultado armazenado:", resultado)


# 5. Verificando se o aluno foi aprovado
media = calcular_media(8, 8, 7)

if media >= 7:
    # Resultado: Aluno aprovado!
    print("Aluno aprovado!")
else:
    # Esta parte não será executada neste exemplo
    print("Aluno reprovado!")


# 6. Usando a função diretamente dentro do print
# Resultado: 7.333333333333333
print(calcular_media(7, 8, 7))


# 7. Chamando a função com valores digitados pelo usuário
nota_a = float(input("Digite a primeira nota: "))
nota_b = float(input("Digite a segunda nota: "))
nota_c = float(input("Digite a terceira nota: "))

media_usuario = calcular_media(nota_a, nota_b, nota_c)

# Resultado: depende das notas digitadas pelo usuário
print("A média das notas é:", media_usuario)
