lista = []
par = []
for c in range(0, 5):
    lista.append(int(input("Digite um número: ")))
for i in lista:
    if i % 2 == 0:
        par.append(i)
print(f"O número 9 aparece {lista.count(9)}")
print(f"O número 3 aparece na posição {lista.index(3)+1}")
print(f"Os números pares são: {par}")