lista = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for c in range(0, 3):
    for i in range(0, 3):
        lista[c][i] = int(input("Digite um número: "))
for c in range(0, 3):
    print("\n")
    for i in range(0, 3):
        print(f"{lista[c][i]:^5}", end=" ")