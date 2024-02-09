def contador(i=0, f=0, p=0):
    print(f"Contagem de {1} até {10} pulando de {1} em {1}: ")
    for c in range(1, 11, 1):
        print(c, end=" ")
    print(f"\nContagem de {10} até {2} pulando de {2} em {2}: ")
    for c in range(10, 0, -2):
        print(c, end=" ")
    print(f"\nContagem de {i} até {f} pulando de {p} em {p}: ")
    if p < 0:
        for c in range(i, f, p):
            print(c, end=" ")
        print(f)
    else:
        for c in range(i, f+i, p):
            print(c, end=" ")
i = int(input("Digite o ínicio: "))
f = int(input("Digite o fim: "))
p = int(input("Digite o passo: "))
contador(i, f, p)