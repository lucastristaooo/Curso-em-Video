from random import randint
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
x = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
x2 = randint(0,5)
print(f'O número sorteado foi {x2}')
x1 = x == x2
if x1:
    True
    print(f'Você ganhou! Eu pensei no número {x2} também!')
else: 
    False
    print(f'Você errou! Eu pensei no número {x2} e você no {x}')