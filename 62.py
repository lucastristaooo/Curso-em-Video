print('Veja a soma de inúmeros valores digitados (-1 PARA PARAR)')
c = 0
cont = 0
while True:
    x = int(input('Digite um número:'))
    cont = cont + 1
    if x == -1:
        break
    c += x
print(f'a soma de {cont-1} valores foi {c}')