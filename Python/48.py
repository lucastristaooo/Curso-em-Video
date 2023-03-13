print("Veja a soma dos 7 valores digitados")
soma = 0
for c in range (1,7):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        soma = soma + x
print(f'A soma de {c} valores, é de {soma}')