lista = []
for c in range(0, 5):
    lista.append(int(input("Digite um número: ")))
print(f"O maior valor foi {max(lista)} na posição {lista.index(max(lista))}")
print(f"O menor valor foi {min(lista)} na posição {lista.index(min(lista))}")