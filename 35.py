print('Transforme seu número')
n = int(input('Escreva um número'))
x = int((input(f'''Escolha o metódo de conversão: 
{1} para binário
{2} para octal
{3} para hexadecimal''')))
if x == 1:
    n2 = bin(n)[2:]
    print(f'{n} convertido para binário é é {n2}')
elif x == 2:
    n2 = oct(n)[2:]
    print(f'{n} convertido para octal é {n2}')
elif x == 3:
    n2 = hex(n)[2:]
    print(f'{n} convertido para hexadecimal é {n2}')
else: print('ERRO, VALOR NÃO ACEITO')