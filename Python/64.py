from random import randint
cont = 0
cont1 = 0
z = str(input('VAMOS JOGAR PAR OU ÍMPAR?')).upper().strip()
while True:
    r = randint(1, 10)
    if z != 'SIM'.upper().strip():
        print('ERRO, VALOR INVÁLIDO')
        break
    if z == 'SIM':
        x = int(input('Digite um número'))
        s = r + x
        y = str(input('Escolha I (ÍMPAR) /P (PAR) OU (SAIR) PARA SAIR:')).upper().strip()
        if y == 'I':
            if s % 2 == 1:
                print(f'Você venceu {s} é ímpar! O adversário jogou {r} e você {x}')
                cont =+ 1
            elif s % 2 == 0:
                print(f'Você perdeu {s} é par! O adversário jogou {r} e você {x}')
                cont =+ 1
        elif y == 'P':
            if s % 2 == 1:
                print(f'Você perdeu {s} é ímpar! O adversário jogou {r} e você {x}')
                cont =+ 1
            elif s % 2 == 0:
                print(f'Você venceu {s} é par! O adversário jogou {r} e você {x}')
                cont =+ 1
        if y == 'SAIR'.upper().strip():
            break
print(f'FIM DE JOGO, SUA PONTUAÇÃO FOI {cont} E A DO COMPUTADOR FOI {cont1}')