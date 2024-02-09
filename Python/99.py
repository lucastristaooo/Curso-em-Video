def maior(*num):
    cont = 0
    for c in num:
        if cont == 0:
            maior = c
            menor = c
        else: 
            if c > maior:
                maior = c
            elif c < menor:
                maior = c
        cont += 1
    print(f"O maior número é {maior}")
    print(f"O menor número é {menor}")
maior(1, 3, 4, 5, 9, 2)
