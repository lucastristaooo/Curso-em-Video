print("Calculadora completa")
x = int(input('Digite um número:'))
y = int(input('Digite outro número:'))
n = 0
while n != 5:
    print('''Escolha:
    [1] Soma
    [2] Multiplicação
    [3] Maior número
    [4] Novos valores
    [5] Sair do programa''')
    n = int(input('Qual vai ser?'))
    if n == 1:
        print(f'A soma é {x + y}')
    elif n == 2:
        print(f'A multiplicação é {x * y}')
    elif n == 3:
        if x > y:
            print(f'O maior é {x}')
        elif y > x:
            print(f'O maior é {y}')
    elif n == 4:
        print('Informe os números novamente:')
        x = int(input('Digite um novo número:'))
        y = int(input('Digite outro novo número:'))
    elif n == 5:
        print('Fechando programa...')
    else:
        print('Valor inválido.')
print('Fim do programa')