# ============================================
# 1. Removendo espaços do início e do final
# ============================================

nome = "   Eduardo   "

nome_limpo = nome.strip()

print(nome_limpo)
# Resultado:
# Eduardo


# ============================================
# 2. Removendo apenas espaços do lado esquerdo
# ============================================

texto = "   Olá, mundo!"

texto_sem_espacos_esquerda = texto.lstrip()

print(texto_sem_espacos_esquerda)
# Resultado:
# Olá, mundo!


# ============================================
# 3. Removendo apenas espaços do lado direito
# ============================================

texto = "Olá, mundo!   "

texto_sem_espacos_direita = texto.rstrip()

print(texto_sem_espacos_direita)
# Resultado:
# Olá, mundo!


# ============================================
# 4. Removendo caracteres específicos
# ============================================

frase = "---Python---"

frase_limpa = frase.strip("-")

print(frase_limpa)
# Resultado:
# Python


# ============================================
# 5. Removendo vários tipos de caracteres
# ============================================

frase = "...Python!!!"

# Remove pontos e exclamações das extremidades.
# Atenção: os caracteres são removidos individualmente.
frase_limpa = frase.strip(".!")

print(frase_limpa)
# Resultado:
# Python


# ============================================
# 6. Usando strip() com quebra de linha
# ============================================

texto = "\nOlá, Python!\n"

texto_limpo = texto.strip()

print(texto_limpo)
# Resultado:
# Olá, Python!


# ============================================
# 7. Removendo símbolos de uma entrada do usuário
# ============================================

email = "   eduardo@email.com   "

email_limpo = email.strip()

print(email_limpo)
# Resultado:
# eduardo@email.com


# ============================================
# 8. Usando strip() antes de comparar textos
# ============================================

resposta = " sim "

# Remove os espaços antes de fazer a comparação.
if resposta.strip() == "sim":
    print("Resposta confirmada!")
# Resultado:
# Resposta confirmada!


# ============================================
# 9. Usando strip() junto com lower()
# ============================================

resposta = "  SIM  "

# strip() remove espaços.
# lower() transforma as letras em minúsculas.
resposta_tratada = resposta.strip().lower()

print(resposta_tratada)
# Resultado:
# sim

if resposta_tratada == "sim":
    print("O usuário respondeu sim.")
# Resultado:
# O usuário respondeu sim.


# ============================================
# 10. Diferença entre strip(), lstrip() e rstrip()
# ============================================

texto = "   Python   "

print(texto.strip())
# Resultado:
# Python

print(texto.lstrip())
# Resultado:
# Python   
# Remove apenas os espaços da esquerda.

print(texto.rstrip())
# Resultado:
#    Python
# Remove apenas os espaços da direita.


# ============================================
# 11. strip() não remove espaços do meio
# ============================================

texto = "Olá    Python"

texto_limpo = texto.strip()

print(texto_limpo)
# Resultado:
# Olá    Python
# Os espaços internos continuam existindo.


# ============================================
# 12. Cuidado: strip() não remove uma palavra inteira
# ============================================

texto = "PythonPython"

# O strip() interpreta "Python" como um conjunto de caracteres.
# Ele pode remover os caracteres P, y, t, h, o e n das extremidades.
resultado = texto.strip("Python")

print(resultado)
# Resultado:
# 
# Por isso, strip() não deve ser usado para remover palavras inteiras.


# ============================================
# 13. Removendo caracteres de pontuação
# ============================================

palavra = "!!!Python???"

palavra_limpa = palavra.strip("!?")

print(palavra_limpa)
# Resultado:
# Python


# ============================================
# 14. Processando vários nomes com strip()
# ============================================

nomes = [" Ana ", " Bruno", "Carla "]

for nome in nomes:
    nome_limpo = nome.strip()
    print(nome_limpo)

# Resultado:
# Ana
# Bruno
# Carla