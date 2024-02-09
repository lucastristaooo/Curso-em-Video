from random import randint
num = randint(0, 10)
cont = 0
while x != num:
    x = int(input("Errado! Tente novamente: "))
    cont += 1
print(f"Parabéns! O número era {num} e você levou {cont} tentativas para acertar")