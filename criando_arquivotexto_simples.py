msg = "text\nOlá mundo!\nEstou aprendendo em Python!"

with open("mensagem2.txt", "w",encoding="utf-8") as arquivo:
    arquivo.write(msg)

with open("mensagem2.txt","r",encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)