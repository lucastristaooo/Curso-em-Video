cont = 0
soma = 0
while True:
    cont += 1
    x = int(input("Digite um número: "))
    if x == 999:
        break
    else:
        soma += x
print(f"Foram digitados {cont} números e a soma de todos é {soma}")