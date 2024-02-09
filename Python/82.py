lista = []
pares = []
ímpares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    x = str(input("Deseja continuar?"))
    if x not in "Ss":
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        ímpares.append(c)
print(f"Lista com todos os números: {lista}")
print(f"Lista com números pares: {pares}")
print(f"Lista com números ímapres {ímpares}")