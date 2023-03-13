print("Vjeja os 10 primeiros termos de uma razão")
pi = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
x = pi + (10 - 1) * r
print('Os 10 primeiros termos dessa razão são: ')
for c in range(pi, x + r, r):
    print(f'{c}')