print("Jogo de adivinhação")
from random import randint
y = randint(1, 10)
tentativas = 0
acertou = False
x = int(input('Digite um número: '))

while not acertou:
    if x == y:
        acertou = True
    tentativas = tentativas + 1
    if x > y:
         x = int(input('Menos... Tente novamente: '))
    elif x < y:
        x = int(input('Mais... Tente novamente:'))
print(f'Sucesso! você acertou em {tentativas} tentativas ')