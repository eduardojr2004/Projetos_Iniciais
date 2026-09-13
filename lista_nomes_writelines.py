nomes = ["Ana\n", "Bruno\n", "Carla\n", "Diego\n", "Eduardo"]

with open("lista_nomes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(nomes)

with open("lista_nomes.txt", "r", encoding="utf-8") as arquivo:
    listagem = arquivo.read()
    print(listagem)