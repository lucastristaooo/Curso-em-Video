from random import randint
lista = []
y = int(input("Quantos jogos você deseja sortear?"))
for c in range(0, y):
    for i in range(0, 6):
        x = randint(0, 60)
        if x not in lista:
            lista.append(x)
    print(f"Jogo {c+1}: {lista}")
    lista.clear()