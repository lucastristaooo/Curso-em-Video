print('Compare que veja qual valor é maior')
x = int(input('Digite um número'))
y = int(input('Digite outro número'))
if x > y:
    print(f'O primeiro valor {x} é maior que {y}')
elif y > x:
    print(f'O segundo valor {y} é maior que {x}')
else:
    print(f'{x} e {y} são valores iguais')