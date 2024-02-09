def fatorial(x):
    soma = 1
    for c in range(x, 0, -1):
        soma *= c
    return soma
print(fatorial(5))
