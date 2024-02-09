from random import randint
lista = []
for c in range(0, 3):
    lista.append(randint(0, 10))
print(f"Maior valor da lista {max(lista)}")
print(f"Menor valor da lista {min(lista)}")