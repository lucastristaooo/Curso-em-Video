cont = 0
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um número:'))
a = int(input('Digite um último número: '))
t = (x, y, z, a)
print(f'Você digitou os valores {t}')
print(f'O número "9" aparece {t.count(9)} vezes')
if 3 in t:
    print(f'O número 3 aparece na {t.index(3)+1} posição')
else:
    print('O número 3 não foi digitado')
for n in t:
    if n % 2 == 0:
        print(f'Os números pares são: {n} ')