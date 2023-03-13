from random import randint
def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
        lista
    print(f"Os valores sorteados foram: {lista}")
def soma(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f"A soma dos valores pares dentro de {lista} é de {soma}")
lista = []
sorteio(lista)
soma(lista)