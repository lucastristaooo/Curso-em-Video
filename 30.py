print('Analisador de triângulos')
x = float(input('Digite o primeiro segmento'))
y = float(input('Digite o segundo segmento'))
z = float(input('Digite o terceiro segmento'))
if y + z < x or z + y < x:
    print('É possível um triângulo ser formado')
if x + z < y or z + x < y:
    print('É possível um triângulo ser formado') 
if x + y < z or y + x < z:
    print('É possível um triângulo ser formado')
else:
    print('Um triângulo não pode ser formado')