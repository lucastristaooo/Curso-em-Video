print('Veja a soma de inúmeros valores digitados (999 PARA PARAR)')
x = 0
cont = 0
soma = 0
while x != 999:
    x = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + x
print(f'A soma de {cont-1} valore(s) é de {soma - 999}')