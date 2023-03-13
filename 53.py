somaidade = 0
nomevelho = {''}
maior = 0
z = 0
for c in range(1,5):
    nome = str(input('Digite seu nome')).upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite seu sexo (Homem/Mulher): ')).upper()
    somaidade += idade
    médiaidade = somaidade / 4
    if c == 1 and 'HOMEM':
        maior = idade
        nomevelho = nome
    if 'HOMEM' and idade > maior:
        maior = idade
        nomevelho = nome
    if sexo == 'MULHER' and idade <= 20:
        z =+ c
print(f'{médiaidade} é a media de idade do grupo')
print(f'{z} é o número de mulheres com menos de 20 anos no grupo')
print(f'{nomevelho} é o homem mais velho do grupo')