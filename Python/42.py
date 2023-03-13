print("Veja o desconto em cada forma de pagamento")
preço = float(input('Digite o valor do produto'))
meio = int(input(f'Digite a forma de pagamento: [1] - Dinheiro ou Cheque, [2] - Cartão, [3] - Cartão em duas vezes, [4] - Cartão em 3 ou mais vezes: '))
dinheiro = preço - (preço * 10) / 100
cartão = preço - (preço * 5) / 100
x2cartão = preço == preço
x3cartão = preço + (preço * 20) / 100
if meio == 1:
    print(f'Seu valor é {dinheiro}R$ com 10% de desconto')
elif meio == 2:
    print(f'Seu valor é {cartão}R$ com 5% de desconto')
elif meio == 3:
    print(f'Seu valor é {x2cartão}R$, sem desconto algum')
else:
    print(f'Seu valor é {x3cartão}R$, com 20% de juros')