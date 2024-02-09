from random import shuffle
lista = []
for c in range(0, 4):
    lista.append(str(input("Digite um nome: ")))
shuffle(lista)
print((lista))  