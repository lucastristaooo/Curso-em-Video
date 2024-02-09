def somapar(*n):
    soma = 0
    for c in n:
        if c % 2 == 0:
            soma += c
    print(f"A tupla sorteada é {n}")
    print(f"A soma dos pares é igual a {soma}")
from random import randint
somapar(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))