numeros = list(range(1,101))

#[(como quer o valor, no exemplo foi *2)(o for para precorrer a lista)(a condição)]
#[(o_que_fazer com cada_elemento) for (cada_elemento) in (sequência)if...]
novos_numeros = [numero for numero in numeros if numero % 7 == 0 or numero % 11 == 0]

print(novos_numeros)