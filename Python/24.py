print('Calcule o preço da sua viagem')
x = int(input('Quantos KM é a sua viagem?'))
if x < 200:
    x1 = x * 0.50
    print(f'O custo da sua viagem vai ser {x1}R$')
else:
    x2 = x * 0.45
    print(f'O custo da sua viagem vai ser {x2}R$')