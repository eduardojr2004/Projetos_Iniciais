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