# Lista com 3 itens
frutas = ["maçã", "banana", "laranja"]


# ==================================================
# 1. Percorrendo cada item da lista
# ==================================================

for fruta in frutas:
    print(fruta)

# Resultado:
# maçã
# banana
# laranja


# ==================================================
# 2. Exibindo uma mensagem para cada item
# ==================================================

for fruta in frutas:
    print(f"Eu gosto de {fruta}.")

# Resultado:
# Eu gosto de maçã.
# Eu gosto de banana.
# Eu gosto de laranja.


# ==================================================
# 3. Contando os itens usando enumerate()
# ==================================================

for numero, fruta in enumerate(frutas, start=1):
    print(f"{numero}º item: {fruta}")

# Resultado:
# 1º item: maçã
# 2º item: banana
# 3º item: laranja


# ==================================================
# 4. Verificando uma condição dentro do for
# ==================================================

for fruta in frutas:
    if fruta == "banana":
        print("Encontrei a banana!")

# Resultado:
# Encontrei a banana!


# ==================================================
# 5. Usando continue para pular um item
# ==================================================

for fruta in frutas:
    if fruta == "banana":
        continue  # Pula a banana e continua o laço

    print(fruta)

# Resultado:
# maçã
# laranja


# ==================================================
# 6. Usando break para interromper o laço
# ==================================================

for fruta in frutas:
    print(fruta)

    if fruta == "banana":
        break  # Interrompe o laço ao encontrar a banana

# Resultado:
# maçã
# banana


# ==================================================
# 7. Criando uma nova lista durante o for
# ==================================================

frutas_maiusculas = []

for fruta in frutas:
    frutas_maiusculas.append(fruta.upper())

print(frutas_maiusculas)

# Resultado:
# ['MAÇÃ', 'BANANA', 'LARANJA']