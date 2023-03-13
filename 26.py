print("Veja se você ultrapassou o limite de velocidade")
x = int(input('Digite a quantos km está o carro'))
m = (x-80) * 7
if x > 80:
    print(f'Você ultrapassou o limite de velocidade :(, e sua multa é de {m:2},00R$')
else:
    print('Você está dentro do limite de velocidade :)')