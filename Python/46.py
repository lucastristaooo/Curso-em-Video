print('Veja a soma de todos os números ímpares de 1 a 50 divisiveis por 3:')
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'É a soma {soma} de {cont} valores')