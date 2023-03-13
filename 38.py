print("Veja sua média")
x = float(input('Digite sua nota'))
y = float(input('Digite sua segunda nota'))
n = (x + y) / 2
if n < 5:
    print(f'REPROVADO: Sua média foi {n}, menor que 5.0')
elif 7 >= n >= 5:
    print(f'RECUPERAÇÃO: Sua média foi {n}, entre 5.0 e 6.9')
elif n >= 7:
    print(f'APROVADO: Sua média foi {n}, entre 7.0 e 10.0')