from time import sleep
from random import randint
cont = 0
soma = 0
while True:
    computador = randint(0, 10)
    jogador = int(input("Digite um número: "))
    escolha = str(input("[PAR] / [ÍMPAR] ")).strip().upper()[0]
    soma = jogador + computador
    if escolha in "Pp":
        if soma % 2 == 0:
            sleep(1)
            print("Você venceu")
            cont += 1
        else:
            sleep(1)
            print("Você perdeu")
            print(f"Suas vitorias são {cont}")
            break
    elif escolha in "Ii":
        if soma % 2 == 1:
            sleep(1)
            print("Você venceu")
        else:
            sleep(1)
            print("Você perdeu")
            print(f"Suas vitórias são {cont}")
            break