print("Veja se o número é ímpar ou par")
x = int(input('Digite um número'))
x1 = x % 2
if x1 == 1:
    print(f'Seu número {x} é ímpar')
else:
    print(f'Seu número {x} é par')