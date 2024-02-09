x = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão"))
for c in range(x, (razao*10)+x, razao):
    print(x, end=" ")
    x+=razao