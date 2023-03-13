print("Veja o maior e o menor peso informados")
n = 0
maior = 0
menor = 0
for c in range(1,6):
    x = float(input(f'Digite o {c}º peso em kg'))
    n +=1
    if c == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
print(f'De {n} pesos informados, {maior}kg é o maior peso')
print(f'De {n} pesos informados, {menor}kg é o menor peso')