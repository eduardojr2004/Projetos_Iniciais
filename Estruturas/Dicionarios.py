# ==========================================
# 1. CRIANDO UM DICIONÁRIO COM 3 ALUNOS
# ==========================================

alunos = {
    "Ana": {
        "idade": 20,
        "nota": 8.5
    },
    "Bruno": {
        "idade": 22,
        "nota": 7.0
    },
    "Carla": {
        "idade": 19,
        "nota": 9.2
    }
}

print(alunos)

# Resultado:
# {
#     'Ana': {'idade': 20, 'nota': 8.5},
#     'Bruno': {'idade': 22, 'nota': 7.0},
#     'Carla': {'idade': 19, 'nota': 9.2}
# }


# ==========================================
# 2. ACESSANDO OS DADOS DE UM ALUNO
# ==========================================

print(alunos["Ana"])

# Resultado:
# {'idade': 20, 'nota': 8.5}


# Acessando somente a idade de Ana

print(alunos["Ana"]["idade"])

# Resultado:
# 20


# Acessando somente a nota de Carla

print(alunos["Carla"]["nota"])

# Resultado:
# 9.2


# ==========================================
# 3. ACESSANDO UMA INFORMAÇÃO COM get()
# ==========================================

print(alunos.get("Bruno"))

# Resultado:
# {'idade': 22, 'nota': 7.0}


# O método get() evita um erro caso a chave não exista

print(alunos.get("Daniel", "Aluno não encontrado"))

# Resultado:
# Aluno não encontrado


# ==========================================
# 4. ALTERANDO A NOTA DE UM ALUNO
# ==========================================

alunos["Bruno"]["nota"] = 8.0

print(alunos["Bruno"])

# Resultado:
# {'idade': 22, 'nota': 8.0}


# ==========================================
# 5. ADICIONANDO UM NOVO ALUNO
# ==========================================

alunos["Daniel"] = {
    "idade": 21,
    "nota": 7.8
}

print(alunos)

# Resultado:
# {
#     'Ana': {'idade': 20, 'nota': 8.5},
#     'Bruno': {'idade': 22, 'nota': 8.0},
#     'Carla': {'idade': 19, 'nota': 9.2},
#     'Daniel': {'idade': 21, 'nota': 7.8}
# }


# ==========================================
# 6. VERIFICANDO SE UM ALUNO EXISTE
# ==========================================

print("Ana" in alunos)

# Resultado:
# True


print("Eduardo" in alunos)

# Resultado:
# False


# ==========================================
# 7. CONTANDO A QUANTIDADE DE ALUNOS
# ==========================================

print(len(alunos))

# Resultado:
# 4


# Neste momento existem 4 alunos,
# pois adicionamos Daniel ao dicionário.


# ==========================================
# 8. LISTANDO SOMENTE OS NOMES DOS ALUNOS
# ==========================================

print(alunos.keys())

# Resultado:
# dict_keys(['Ana', 'Bruno', 'Carla', 'Daniel'])


# Convertendo as chaves para uma lista

print(list(alunos.keys()))

# Resultado:
# ['Ana', 'Bruno', 'Carla', 'Daniel']


# ==========================================
# 9. LISTANDO SOMENTE OS DADOS DOS ALUNOS
# ==========================================

print(alunos.values())

# Resultado:
# dict_values([
#     {'idade': 20, 'nota': 8.5},
#     {'idade': 22, 'nota': 8.0},
#     {'idade': 19, 'nota': 9.2},
#     {'idade': 21, 'nota': 7.8}
# ])


# ==========================================
# 10. LISTANDO NOMES E DADOS AO MESMO TEMPO
# ==========================================

print(alunos.items())

# Resultado:
# dict_items([
#     ('Ana', {'idade': 20, 'nota': 8.5}),
#     ('Bruno', {'idade': 22, 'nota': 8.0}),
#     ('Carla', {'idade': 19, 'nota': 9.2}),
#     ('Daniel', {'idade': 21, 'nota': 7.8})
# ])


# ==========================================
# 11. PERCORRENDO O DICIONÁRIO COM for
# ==========================================

for nome, dados in alunos.items():
    print(nome, dados)

# Resultado:
# Ana {'idade': 20, 'nota': 8.5}
# Bruno {'idade': 22, 'nota': 8.0}
# Carla {'idade': 19, 'nota': 9.2}
# Daniel {'idade': 21, 'nota': 7.8}


# ==========================================
# 12. MOSTRANDO UMA FRASE PARA CADA ALUNO
# ==========================================

for nome, dados in alunos.items():
    print(f"{nome} tem {dados['idade']} anos e tirou nota {dados['nota']}.")

# Resultado:
# Ana tem 20 anos e tirou nota 8.5.
# Bruno tem 22 anos e tirou nota 8.0.
# Carla tem 19 anos e tirou nota 9.2.
# Daniel tem 21 anos e tirou nota 7.8.


# ==========================================
# 13. REMOVENDO UM ALUNO COM pop()
# ==========================================

aluno_removido = alunos.pop("Daniel")

print(aluno_removido)

# Resultado:
# {'idade': 21, 'nota': 7.8}


print(alunos)

# Resultado:
# {
#     'Ana': {'idade': 20, 'nota': 8.5},
#     'Bruno': {'idade': 22, 'nota': 8.0},
#     'Carla': {'idade': 19, 'nota': 9.2}
# }


# ==========================================
# 14. REMOVENDO O ÚLTIMO ITEM COM popitem()
# ==========================================

ultimo_aluno = alunos.popitem()

print(ultimo_aluno)

# Resultado:
# ('Carla', {'idade': 19, 'nota': 9.2})


print(alunos)

# Resultado:
# {
#     'Ana': {'idade': 20, 'nota': 8.5},
#     'Bruno': {'idade': 22, 'nota': 8.0}
# }


# ==========================================
# 15. ADICIONANDO CARLA NOVAMENTE
# ==========================================

alunos["Carla"] = {
    "idade": 19,
    "nota": 9.2
}

print(alunos)

# Resultado:
# {
#     'Ana': {'idade': 20, 'nota': 8.5},
#     'Bruno': {'idade': 22, 'nota': 8.0},
#     'Carla': {'idade': 19, 'nota': 9.2}
# }


# ==========================================
# 16. CALCULANDO A MÉDIA DAS NOTAS
# ==========================================

soma_notas = 0

for dados in alunos.values():
    soma_notas += dados["nota"]

media = soma_notas / len(alunos)

print(media)

# Resultado:
# 8.566666666666666


# ==========================================
# 17. ARREDONDANDO A MÉDIA
# ==========================================

print(round(media, 2))

# Resultado:
# 8.57


# ==========================================
# 18. VERIFICANDO QUAIS ALUNOS FORAM APROVADOS
# ==========================================

for nome, dados in alunos.items():
    if dados["nota"] >= 7:
        print(f"{nome} foi aprovado.")

# Resultado:
# Ana foi aprovado.
# Bruno foi aprovado.
# Carla foi aprovado.


# ==========================================
# 19. LIMPANDO TODO O DICIONÁRIO
# ==========================================

# O método clear() remove todos os alunos.

alunos.clear()

print(alunos)

# Resultado:
# {}



# {}	Cria o dicionário
# :	Separa chave e valor
# ,	Separa os itens
# []	Acessa um valor pela chave
# ()	Executa uma função ou agrupa argumentos