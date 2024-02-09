from random import randint
lista = []
for c in range(0, 4):
    x = int(input("Digite um número: "))
    lista.append(x)
print(f"O número sorteado foi {randint(lista[0],lista[3])}")