lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    x = str(input("Deseja continuar?"))
    if x not in "Ss":
        break
print(f"A média dos valores é de: {sum(lista)/len(lista)}")
print(f"Maior valor: {max(lista)} Menor valor: {min(lista)}")
