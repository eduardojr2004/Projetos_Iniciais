n = int(input("Informe o número inteiro: "))
atual = 1
anterior = 0
cont = 0

print(f"Os primeiros {n} termos da sequência de Fibonacci são:")
while cont < n:
    print((atual), end=(" "))
    novo_termo = anterior + atual
    anterior = atual
    atual = novo_termo
    cont = cont + 1