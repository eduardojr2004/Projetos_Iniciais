valor = int(input("Informe o valor a ser sacado: "))
sacar = 0
cinquenta = 0
vinte = 0
dez = 0
um = 0

while (valor > sacar) and ((sacar + 50) <= valor):
    sacar = sacar + 50
    cinquenta = cinquenta + 1

while (valor > sacar) and ((sacar + 20) <= valor):
    sacar = sacar + 20
    vinte = vinte + 1

while (valor > sacar) and ((sacar + 10) <= valor):
    sacar = sacar + 10
    dez = dez + 1

while (valor > sacar) and ((sacar + 1) <= valor):
    sacar = sacar + 1
    um = um + 1

print(
    f"Foram utilizadas: \n"
    f"{cinquenta} nota(s) de R$ 50 \n"
    f"{vinte} nota(s) de R$ 20 \n"
    f"{dez} nota(s) de R$ 10 \n"
    f"{um} nota(s) de R$ 1."
)