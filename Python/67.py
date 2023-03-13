x = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= x <= 20:
        break
    else:
        x = int(input('Tente novamente, digite um número entre 0 e 20: '))
p = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'Você escreveu o número {p[x]}')
