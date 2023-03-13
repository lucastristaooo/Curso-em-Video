cont = maior = menor = média = soma = 0
n1 = str(input('Quer começar? {SIM} ou [NÃO]')).upper()
if n1 == 'SIM'.upper():
    print('Carregando...')
elif n1 == 'NÃO':
    print('Ok!')
else:
    print('ERRO, VALOR INVÁLIDO')

while n1 == 'SIM':
    n = int(input('Digite um número: '))
    n1 = str(input('Quer continuar? [SIM] ou [NÃO]')).upper()
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    if n1 == 'NÃO':
        média = soma / cont
        print(f'Você digitou {cont} valores e a média foi {média}')
        print(f'O maior valor é {maior} e o menor valor é {menor}')