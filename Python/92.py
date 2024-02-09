from datetime import datetime
dict = {}
dict["nome"] = str(input("Digite o nome: "))
dict["idade"] = int(input("Digite o ano de nascimento: "))
dict["carteira"] = int(input("Digite a carteira de trabalho (0 Não tem): "))
if dict["carteira"] == 0:
    dict["idade"] = 2023 - dict["idade"]
    for i, c in dict.items():
        print(f"{i} é igual a {c}") 
else:
    dict["contratação"] = int(input("Digite o ano de contratação: "))    
    dict["salário"] = float(input("Digite o salário R$: "))
    dict["idade"] = datetime.now().year - dict["idade"]
    dict["ano de aposentadoria"] = dict["idade"] + ((dict["contratação"] + 35) - datetime.now().year)
    for c, k in dict.items():
        print(f"{c} é {k}")