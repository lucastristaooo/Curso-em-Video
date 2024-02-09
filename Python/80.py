import bisect
números = []
for i in range(5):
    n = int(input("Digite um número: "))
    bisect.insort(números, n)
    print(f"Número {n} incluido na posição {números.index(n)}")
print(f"Números digitados: {números}")