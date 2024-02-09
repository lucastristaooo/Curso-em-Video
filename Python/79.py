lista = []
for c in range(0, 5):
    x = int(input("Digite um número: "))
    if x not in lista:
        print("Valor não repetido, adicionado com sucesso!")
        lista.append(x)
print(sorted(lista))