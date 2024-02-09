dict = {}
lista = []
mulheres = []
soma = 0
while True:
    dict["nome"] = str(input("Digite o nome: "))
    dict["sexo"] = str(input("Digite o sexo (M/F):")).strip().upper()
    while dict["sexo"][0] not in "MF":
        dict["sexo"] = str(input("Digite o sexo (M/F):")).strip().upper()
    dict["idade"] = int(input("Digite a idade: "))
    if dict["sexo"] == "F":
        mulheres.append(dict["nome"])
    soma += dict["idade"]
    lista.append(dict.copy())
    continuar = str(input("Deseja continuar? (S/N)")).strip().upper()
    while continuar not in "SN":
        continuar = str(input("Deseja continuar? (S/N)")).strip().upper()
    if continuar == "N":
        break
print(f"Ao todo temos {len(lista)} pessoas cadastradas")
print(f"A média da idade é de {soma/len(lista)}")
print(f"As mulheres cadastradas foram {mulheres}")
print(f"Lista de pessoas que estão acima da média: ")
for i in lista:
    if i["idade"] >= soma/len(lista):
        print(i)
