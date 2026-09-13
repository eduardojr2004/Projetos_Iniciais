produtos = ["Arroz - R$ 25.90\n",
            "Feijão - R$ 8.50\n", 
            "Leite - R$ 4.75\n", 
            "Tomate - R$ 6.99\n", 
            "Maçã - R$ 7.49"]

with open("lista_produtos.txt", "w", encoding="utf-8") as arquivo:
    arquivo.writelines(produtos)

with open("lista_produtos.txt", "r", encoding="utf-8") as arquivo:
    leitura = arquivo.readlines()
    
for numero, produto in enumerate(leitura, start = 1):
    print(f"{numero}. {produto}",end="")