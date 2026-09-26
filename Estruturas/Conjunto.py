# Criando um conjunto com 3 linguagens de programação
linguagens = {"Python", "Java", "JavaScript"}

# Exibindo o conjunto
# A ordem pode variar, pois conjuntos não são ordenados.
print(linguagens)

# Resultado possível:
# {'Python', 'Java', 'JavaScript'}


# --------------------------------------------------
# 1. Verificando a quantidade de itens
# --------------------------------------------------

quantidade = len(linguagens)

print(quantidade)

# Resultado:
# 3


# --------------------------------------------------
# 2. Verificando se um item existe no conjunto
# --------------------------------------------------

print("Python" in linguagens)

# Resultado:
# True


print("C++" in linguagens)

# Resultado:
# False


# --------------------------------------------------
# 3. Adicionando um novo item
# --------------------------------------------------

linguagens.add("C++")

# Usamos sorted() apenas para exibir os itens em ordem alfabética.
print(sorted(linguagens))

# Resultado:
# ['C++', 'Java', 'JavaScript', 'Python']


# --------------------------------------------------
# 4. Tentando adicionar um item que já existe
# --------------------------------------------------

linguagens.add("Python")

print(sorted(linguagens))

# Resultado:
# ['C++', 'Java', 'JavaScript', 'Python']
#
# O item "Python" não foi duplicado.


# --------------------------------------------------
# 5. Removendo um item com remove(), melhor usar discard() abaixo 👇 
# --------------------------------------------------

linguagens.remove("Java")

print(sorted(linguagens))

# Resultado:
# ['C++', 'JavaScript', 'Python']


# --------------------------------------------------
# 6. Removendo um item com discard()
# --------------------------------------------------

linguagens.discard("C++")

print(sorted(linguagens))

# Resultado:
# ['JavaScript', 'Python']


# A diferença é que discard() não causa erro
# caso o item não exista no conjunto.
linguagens.discard("Ruby")

print(sorted(linguagens))

# Resultado:
# ['JavaScript', 'Python']


# --------------------------------------------------
# 7. Verificando se o conjunto está vazio
# --------------------------------------------------

print(len(linguagens) == 0)

# Resultado:
# False


# --------------------------------------------------
# 8. Limpando todos os itens do conjunto
# --------------------------------------------------

linguagens.clear()

print(linguagens)

# Resultado:
# set()


# --------------------------------------------------
# 9. Verificando novamente se o conjunto está vazio
# --------------------------------------------------

print(len(linguagens) == 0)

# Resultado:
# True