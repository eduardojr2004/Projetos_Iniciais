import random
num = random.randint(0, 50)
selecionado = None

while selecionado != num:
    selecionado = int(input("Escolha um número entre 0 e 50: "))

    if(selecionado > num):
       print("O número selecionado é maior")
       
    elif(selecionado < num):
        print("O número selecionado é menor")
        
print(f"Você acertou! O número é: {num}!")