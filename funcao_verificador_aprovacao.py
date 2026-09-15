def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

def verificar_aprovacao(media):
    return media >= 7

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))

media = calcular_media(n1,n2,n3)

situacao = verificar_aprovacao(media)

if situacao:
    print(f"A média do aluno(a) foi: {media:.2f}, aprovado(a)")
else:
    print(f"A média do aluno(a) foi: {media:.2f}, desaprovado(a)")