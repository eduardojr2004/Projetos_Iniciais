frase = "A programação Python é interessante."

resul = frase.strip().replace(" ","")

for i in resul:
    if i in "aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ":
        continue
    print(i)