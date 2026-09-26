from math import sqrt
from funcao_triangulo import funcao_triangulo

l1 = float(input(f"Informe o primeiro lado: "))
l2 = float(input(f"Informe o segundo lado: "))
l3 = float(input(f"Informe o terceiro lado: "))

triangulo = funcao_triangulo(l1,l2,l3)

if triangulo:
    perimetro = l1 + l2 + l3
    semiperimetro = perimetro / 2

    area = sqrt(
        semiperimetro
        * (semiperimetro - l1)
        * (semiperimetro - l2)
        * (semiperimetro - l3)
    )

    print(
        f"As medidas foram um triângulo!"
        f"\nPerímetro: {perimetro}"
        f"\nÁrea: {area:.2f}"
        )

else:
    print("NÃO é um triângulo!")