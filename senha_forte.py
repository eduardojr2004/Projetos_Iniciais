senha = input("Informe a senha: ")
tem_digito = False
tem_maiuscula = False
tem_minuscula = False
tem_especial = False

for i in senha:
    if i.isupper():
        tem_maiuscula = True
        
    elif i.islower():
        tem_minuscula = True
    
    elif i.isdigit():
        tem_digito = True

    elif i in "@#$%!?":
        tem_especial = True

if (len(senha) >= 8
    and tem_maiuscula
    and tem_minuscula
    and tem_digito
    and tem_especial):
    print("A senha é segura!")
else:
    print("A senha NÃO é segura!")