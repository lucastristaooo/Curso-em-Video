print('Calcule um aumento de 10% ou 15%')
x = float(input('Digite o seu salário'))
base = 1250
if x < base:
    y = (x * 15) / 100 + x
    print(f'Seu novo salário é de {y} com um aumento de 15%')
else:
    z = (x * 10) / 100 + x
    print(f'Seu novo salário é de {z} com um aumento de 10%')