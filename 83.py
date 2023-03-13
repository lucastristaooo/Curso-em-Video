dict = {}
lista = []
media = 0
soma = 0
while True:
    dict.clear()
    dict['nome'] = str(input("Digite seu nome: "))
    dict['sexo'] = str(input("Digite seu sexo(M/F)"))
    while dict['sexo'] not in 'MF':
        dict['sexo'] = str(input("Erro, valor inválido, digite seu sexo(M/F)"))
    dict['idade'] = int(input("Digite sua idade: "))
    soma += dict['idade']
    lista.append(dict.copy())
    x = str(input("Deseja continuar? (S/N)"))
    while x not in 'SN':
        x = str(input("Erro, valor inválido, deseja continuar? (S/N)"))
    if x in 'N':
        break   
print(f"O número de usúarios cadastrados é de {len(lista)}")
print(f"As mulheres cadastradas foram: ")
for dict in lista:
    if dict['sexo'] == 'F':
        print(f"{dict['nome']}")
media = soma / len(lista)
print(f"A média de idade é de {media}")
print(f"As pessoas superiores a média do grupo são: ")
for dict in lista:
    if dict['idade'] >= media:
        for k, v in dict.items():
            print(f'{k} = {v};', end=' ')
        print(' ')
print("PROGRAMA ENCERRADO")