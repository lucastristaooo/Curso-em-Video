dict = {}
lista = []
for c in range(0, 3):
    dict['nome'] = str(input("Digite o nome: "))
    dict['idade'] = int(input("Digite a idade: "))
    lista.append(dict.copy())
print(lista) 