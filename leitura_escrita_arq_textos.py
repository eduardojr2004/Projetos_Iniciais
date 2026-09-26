#PRECISA FECHAR O ARQUIVO
arquivo = open("mensagem.txt","r")
msg = arquivo.read()
arquivo.close()
print(msg)

#FECHA O ARQUIVO AUTOMATICO PASSANDO O CAMINHO DO ARQUIVO, PARA LEITURA PRECISA ATRIBUIR O CONTEÚDO PARA UM VARIÁVEL
caminho = ("E:\Meu Drive\Pessoal\Programacao\GitHub\Projetos_Iniciais\mensagem","r")
with open(caminho, 'r') as arq:
    m = arq.read()
print("-  -  -  -  -  -  -  -")
print(m)

#FECHA O ARQUIVO AUTOMATICO, CRIANDO O ARQUIVO
msg = "text, Olá mundo! Estou aprendendo em Python!"
with open("mensagem2.txt", "w",encoding="utf-8") as arquivo:
    arquivo.write(msg)