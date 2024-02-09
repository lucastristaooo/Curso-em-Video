lista = []
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        lista.append(num)
    x = str(input("Deseja continuar?"))
    if x not in "Ss":
        break
print(f"Você digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Os valores emm ordem decrescente são: {lista}")
if 5 not in lista:
    print("O número 5 não se encontra na lista")
else:
    print(f"O número 5 está na lista, na posição {lista.index(5)}")