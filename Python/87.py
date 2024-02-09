lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
soma = 0
soma3 = 0
maior = 0
for c in range(0, 3):
    for i in range(0, 3):
        lista[c][i] = int(input("Digite um número: "))
        soma += lista[c][i]
        if lista[c][i] % 3 == 0:
            soma3 += lista[c][i]
        if lista[1][i] > maior:
            maior = lista[1][i]
for c in range(0, 3):
    print("\n")
    for i in range(0, 3):
        print(f"{lista[c][i]:^5}", end=" ")
print("\n")
print(f"A soma de todos os valores da matriz é igual a {soma}")
print(f"A soma dos valores da terceira coluna é igual a {soma3}")
print(f"O maior valor da segunda linha é {maior}")