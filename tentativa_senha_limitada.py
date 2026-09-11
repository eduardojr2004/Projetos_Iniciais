cont = 0
password = 1234

while cont < 3:
    senha = int(input("Informe a senha: "))
    if senha == password:
        print("Login Efetuado!")
        break
    else:
         cont += 1
         print("Senha incorreta!")

if cont == 3:
    print("Tentativas excedidas!")