def funcao_triangulo(l1,l2,l3):

    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        return False

    return(
        l1 + l2 > l3
        and l1 + l3 > l2
        and l2 +l3 > l1
    )


def triangulo_vertice(p1, p2, p3):
    
    # Separa as coordenadas do primeiro ponto
    x1, y1 = p1

    # Separa as coordenadas do segundo ponto
    x2, y2 = p2

    # Separa as coordenadas do terceiro ponto
    x3, y3 = p3

    # Calcula o dobro da área do triângulo
    dobro_area = (
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    )

    # Se o resultado for diferente de zero,
    # os pontos não estão alinhados
    return dobro_area != 0