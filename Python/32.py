print('Veja qual o maior e o menor número digitados')
x = int(input('Digite um número'))
y = int(input('Digite um outro número'))
z = int(input('Digite um último número'))
if x > y and x > z:
    maior = x  
if y > x and y > z:
    maior = y  
if z > x and z > y:
    maior = z
print(f'Seu maior número é {maior}')
if x < y and x < z:
    menor = x
if y < x and y< z:
    menor = y
if z < x and z < y:
    menor = z
print(f'Seu menor número foi {menor}')
