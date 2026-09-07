senha = int(1234)

tentativa = int(input("Informe a senha: "))

while tentativa != senha:
    tentativa = int(input("Informe novamente a senha: "))
    print("Novo Login Realizado!")

print("Login realizado!")