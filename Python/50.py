soma = 0
cont = 0
for c in range(0, 6):
    x = int(input("Digite um número: "))
    if x % 2 == 0:
        soma += x
        cont += 1
print(f"Você informou {cont} números pares e a soma foi {soma}")