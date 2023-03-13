print('Veja em qual categoria você se encaixa.')
x = int(input('Digite sua idade'))
if x < 2:
    print('Você não tem idade suficiente para competir')
elif x < 14:
    print('Você se encaixa na categoria MIRIM')
elif x <= 14:
    print('Você se encaixa na categoria INFANTIL')
elif x <= 19:
    print('Você se encaixa na categoria JUNIOR')
else:
    print('Você se encaixa na categoria MASTER')