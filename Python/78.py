from random import randint
lista  = []
print("JOGUE NA MEGA SENA")
x = int(input("Digite quantos jogos deseja fazer: "))
for c in range(x):
    while len(lista) < 6:
        p = randint(1, 60)
        if p not in lista:
            lista.append(p)
    print(f"Lista {c+1}: {(sorted(lista))}")
    lista.clear()