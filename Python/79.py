lista = []
cont = 0
x = str(input("Deseja começar? (S/N)")).strip().upper()
while x == 'S':
    lista.append(str(input("Digite um nome: ")))
    lista.append(float(input("Digite a primeira nota: ")))
    lista.append(float(input("Digite a segunda nota : ")))
    lista.append(float((lista[1] + lista[2]) / 2))
    cont += 1
    p = print(f"Nome: {lista[0]} - Média: {lista[3]}")
    print(f"P1 = {lista[1]}")
    print(f"P2 = {lista[2]}")
    lista.clear()
    x = str(input("Deseja continuar? (S/N)")).strip().upper()
    if x != 'S':
        break