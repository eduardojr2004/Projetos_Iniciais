numeros = list(range(1,101))

#[(como quer o valor, no exemplo foi *2)(o for para precorrer a lista)(a condição)]
novos_numeros = [numero for numero in numeros if numero % 7 == 0 or numero % 11 == 0]

print(novos_numeros)