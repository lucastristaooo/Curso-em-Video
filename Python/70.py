total = mais1000 = menor = cont = 0
menornome = " "
while True:
    produto = str(input("Digite o nome do produto: "))
    preço = int(input("Digite o preço do produto: "))
    cont += 1
    total += preço
    if preço > 1000:
        mais1000 += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            menornome = produto
    x = str(input("Deseja continuar?")).strip().upper()
    while x not in "Ss":
        x = str(input("Deseja continuar?")).strip().upper()
    if x == "N":
        break
print(f"O preço total foi de: {total}")
print(f"Temos {mais1000} items que custaram mais de R$1000,00")
print(f"O produto mais barato foi {menornome} custando {menor}")    