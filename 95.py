dict = {}
lista = []
maior = 0
for c in range(0, 2):
    dict["nome"] = str(input("Digite o nome: "))
    dict["ponto"] = int(input("Digite a pontuação: "))
    lista = dict.copy()
for dict in lista:
    if dict["ponto"] > maior:
        maior = dict["ponto"]
        print(dict["nome"])