# Lista original com 3 alunos
alunos = ["Ana", "Bruno", "Carlos"]


# 1. Percorrer e exibir cada item da lista
for aluno in alunos:
    print(aluno)

# Resultado:
# Ana
# Bruno
# Carlos


# 2. Exibir uma mensagem personalizada para cada aluno
for aluno in alunos:
    print(f"O aluno {aluno} está matriculado.")

# Resultado:
# O aluno Ana está matriculado.
# O aluno Bruno está matriculado.
# O aluno Carlos está matriculado.


# 3. Transformar os nomes em letras maiúsculas
for aluno in alunos:
    print(aluno.upper())

# Resultado:
# ANA
# BRUNO
# CARLOS


# 4. Exibir o número da posição e o nome do aluno
for indice, aluno in enumerate(alunos):
    print(indice, aluno)

# Resultado:
# 0 Ana
# 1 Bruno
# 2 Carlos


# 5. Criar uma nova lista com os nomes em letras maiúsculas
alunos_maiusculos = []

for aluno in alunos:
    alunos_maiusculos.append(aluno.upper())

print(alunos_maiusculos)

# Resultado:
# ['ANA', 'BRUNO', 'CARLOS']


# 6. Verificar se existe um aluno chamado "Bruno"
for aluno in alunos:
    if aluno == "Bruno":
        print("Bruno foi encontrado!")

# Resultado:
# Bruno foi encontrado!


# 7. Exibir somente os alunos cujo nome começa com a letra "C"
for aluno in alunos:
    if aluno.startswith("C"):
        print(aluno)

# Resultado:
# Carlos


# 8. Contar a quantidade de alunos
quantidade = 0

for aluno in alunos:
    quantidade += 1

print(f"Quantidade de alunos: {quantidade}")

# Resultado:
# Quantidade de alunos: 3
