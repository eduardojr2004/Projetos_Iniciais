def calcular_media(n1,n2,n3):
    media = (n1 + n2 + n3) / 3
    return media

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
media = calcular_media(n1,n2,n3)

print(f"A média é {media:.2f}")