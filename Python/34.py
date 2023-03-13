print('Programa para aprovar um impréstimo bancário')
vdc = float(input('Valor da casa: R$'))
s = float(input('Seu salário: R$'))
qs = int(input('Em quantos anos você vai pagar?'))
prest = vdc / (qs * 12)
min = s * 30 / 100
if min > prest:
    print(f'''Parabéns! Você pode conseguir o impréstimo com uma renda de {s:.2f}R$''')
elif min < prest:
    print(f'''Infelizmente você não conseguirá um empréstimo, para pagar uma casa de {vdc:.2f}R$ em {qs} anos você precisaria de uma renda de {prest:.2f}R$ por mês''')