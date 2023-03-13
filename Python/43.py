print('Jogue Pedra, Papel ou Tesoura')
n1 = str(input('''Escolha:
[1] Pedra
[2] Papel
[3] Tesoura''')).strip().upper()
import random
lista = ['PEDRA', 'PAPEL', 'TESOURA']
n2 = (random.choice(lista))
if (n1 not in lista):
    print('ERRO, VALOR NÃO ACEITO, JOGUE NOVAMENTE') 
if n1 == 'PEDRA' and n2 == 'TESOURA':
    print('JA KEN PO')
    print(f'Você venceu! o computador escolheu {n2}')
elif n1 == 'PEDRA' and n2 == 'PAPEL':
    print('JA KEN PO')
    print(f'Você perdeu! o computador escolheu {n2}')
elif n1 == 'PAPEL' and n2 == 'PEDRA':
    print('JA KEN PO')
    print(f'Você venceu! o computador escolheu {n2}')
elif n1 == 'PAPEL' and n2 == 'TESOURA':
    print('JA KEN PO')
    print(f'Você perdeu! o computador escolheu {n2}')
elif n1 == 'TESOURA' and n2 == 'PEDRA':
    print('JA KEN PO')
    print(f'Você perdeu! o computador escolheu {n2}')
elif n1 == 'TESOURA' and n2 == 'PAPEL':
    print('JA KEN PO')
    print(f'Você venceu! o computador escolheu {n2}')
elif n1 == n2:
    print('JA KEN PO')
    print('EMPATE! JOGUE NOVAMENTE')