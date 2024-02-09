lista = []
while True:
    x = int(input("Digite um número: "))
    if x == 999:
        break
    else:
        lista.append(x)
        sum(lista)
    print(f"Foram digitados {len(lista)} e a soma entre eles é igual a {sum(lista)}")