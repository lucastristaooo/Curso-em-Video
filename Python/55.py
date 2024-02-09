lista = []
for c in range(0, 4):
    lista.append(input(f"Digite o peso da pessoa número {c}: "))
print(f"Maior peso: {max(lista)}")
print(f"Mneor peso: {min(lista)}")