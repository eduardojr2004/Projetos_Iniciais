from funcao_triangulo import triangulo_vertice
import re

with open("triangulo_vertices.txt", "r", encoding="utf-8") as arq:
    linhas = arq.readlines()

respostas = []

for linha in linhas:
    linha = linha.replace("−", "-")

    partes = re.findall(r"\((.*?)\)", linha)

    vertices = [
        tuple(map(int, parte.split(",")))
        for parte in partes
    ]

    respostas.append(vertices)


for indice, grupo in enumerate(respostas, start = 1):
    p1, p2, p3 = grupo

    print(f"Grupo {indice}:")
    print(f"  Primeiro ponto: {p1}")
    print(f"  Segundo ponto: {p2}")
    print(f"  Terceiro ponto: {p3}")

    resultado = triangulo_vertice(p1, p2, p3)

    if resultado:
        print(f"  Forma um triângulo")

    else:
        print(f"  NÃO forma um triângulo")