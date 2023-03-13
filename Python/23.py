print('Calcule a casas de um número')
número = int(input('Digite um número:  '))
u = número // 1 % 10
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print(f'Analisando o número {número}')
print(f'Unidade = {u}')
print(f'Dezena = {d}')
print(f'Centena = {c}')
print(f'Milhar = {m}')