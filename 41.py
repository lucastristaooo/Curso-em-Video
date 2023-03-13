print('Analisador de triângulos')
x = float(input('Digite um valor:'))
y = float(input('Digite outro valor'))
z = float(input('Digite outro valor'))
if x < y + z or y < x + z and z < y + x:
    print('É possível um triângulo ser formado')
    if x == y == z:
        print('É um triângulo Equilátero')
    elif x != y != z != x:
        print('É um triângulo Escaleno')
    else:
        print('É um triângulo Isóceles')
else:
    print('Um triângulo não pode ser formado')