nomes = []
pesos = []
maisleves = []
maispesados = []
cont = 0
while True:
    nomes.append(str(input("Digite um nome: ")))
    pesos.append(int(input("Digite o peso: ")))
    cont += 1
    x = str(input("Deseja continuar?"))
    if x not in "Ss":
        break
maispesados.append(nomes[pesos.index(max(pesos))])
maisleves.append(nomes[pesos.index(min(pesos))])
print(f"O número de pessoas cadastradas foi de {cont}")
print(f"A pessoa mais pesada é: {maispesados} com {max(pesos)}kg")
print(f"A pessoa mais leve é: {maisleves} com {min(pesos)}kg ")