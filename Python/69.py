homens = 0
mulheres = 0
mais18 = 0
while True:
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Digite o sexo: ")).strip().upper()
    while sexo not in 'MF':
        sexo = str(input("Sexo inválido, tente novamente: ")).strip().upper()
    if sexo == "M":
        homens += 1
    elif sexo == "F" and idade >= 20:
        mulheres += 1
    if idade >= 18:
        mais18 += 1
    x = str(input("Deseja continuar?")).strip().upper()
    while x not in 'SN':
        x = str(input("Deseja continuar?")).strip().upper()
    if x == "N":
        break
print("Fim do Programa")
print(f"Quantidade de homens cadastrados: {homens}")
print(f"Quantidade de mulheres com mais de 20 anos cadastradas: {mulheres}")
print(f"Quantidade de pessoas com mais de 18 anos cadastrada: {mais18}")