# ==========================================
# 1. Dividir uma frase usando os espaços
# ==========================================

frase = "Eu estou aprendendo Python"

resultado = frase.split()

print(resultado)

# Resultado:
# ['Eu', 'estou', 'aprendendo', 'Python']


# ==========================================
# 2. Dividir usando uma vírgula
# ==========================================

nomes = "Ana,Bruno,Carlos"

resultado = nomes.split(",")

print(resultado)

# Resultado:
# ['Ana', 'Bruno', 'Carlos']


# ==========================================
# 3. Dividir usando ponto e vírgula
# ==========================================

produtos = "arroz;feijão;macarrão"

resultado = produtos.split(";")

print(resultado)

# Resultado:
# ['arroz', 'feijão', 'macarrão']


# ==========================================
# 4. Dividir usando hífen
# ==========================================

data = "20-09-2026"

resultado = data.split("-")

print(resultado)

# Resultado:
# ['20', '09', '2026']


# ==========================================
# 5. Acessar um item da lista criada
# ==========================================

frase = "Python é poderoso"

palavras = frase.split()

print(palavras[0])

# Resultado:
# Python

print(palavras[2])

# Resultado:
# poderoso


# ==========================================
# 6. Usar split() com várias palavras
# ==========================================

frase = "maçã banana laranja uva"

frutas = frase.split()

print(frutas)

# Resultado:
# ['maçã', 'banana', 'laranja', 'uva']

print(frutas[1])

# Resultado:
# banana


# ==========================================
# 7. Dividir somente uma vez
# ==========================================

frase = "Python é uma linguagem de programação"

resultado = frase.split(" ", 1)

print(resultado)

# Resultado:
# ['Python', 'é uma linguagem de programação']

# O número 1 indica que apenas uma divisão deve ser feita.


# ==========================================
# 8. Dividir somente duas vezes
# ==========================================

frase = "Python é uma linguagem de programação"

resultado = frase.split(" ", 2)

print(resultado)

# Resultado:
# ['Python', 'é', 'uma linguagem de programação']

# O número 2 indica que serão feitas, no máximo, duas divisões.


# ==========================================
# 9. Separar uma frase usando ponto
# ==========================================

texto = "Primeira frase. Segunda frase. Terceira frase."

frases = texto.split(".")

print(frases)

# Resultado:
# ['Primeira frase', ' Segunda frase', ' Terceira frase', '']


# ==========================================
# 10. Remover espaços extras antes de dividir
# ==========================================

frase = "   Python é fácil   "

# strip() remove espaços no início e no final
frase_limpa = frase.strip()

# split() divide a frase em palavras
palavras = frase_limpa.split()

print(palavras)

# Resultado:
# ['Python', 'é', 'fácil']


# ==========================================
# 11. Dividir um e-mail
# ==========================================

email = "aluno@escola.com"

partes = email.split("@")

print(partes)

# Resultado:
# ['aluno', 'escola.com']

print(partes[0])

# Resultado:
# aluno

print(partes[1])

# Resultado:
# escola.com


# ==========================================
# 12. Dividir uma extensão de arquivo
# ==========================================

arquivo = "relatorio.pdf"

partes = arquivo.split(".")

print(partes)

# Resultado:
# ['relatorio', 'pdf']

nome = partes[0]
extensao = partes[1]

print(nome)

# Resultado:
# relatorio

print(extensao)

# Resultado:
# pdf