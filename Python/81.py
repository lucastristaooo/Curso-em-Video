dict = {}
dict['nome'] = str(input("Digite seu nome: "))
dict['idade'] = int(input("Digite sua idade: "))
dict['carteira'] = str(input("Digite sua carteira de trabalho: "))
if len(dict['carteira']) > 3:
    dict['ano'] = int(input("Digite o ano de contratação: "))
    dict['salário'] = float(input("Digite seu salário: "))
    dict['aposentadoria'] = (dict['ano'] + dict['idade'] + 35) - 2022
else:
    print("Você não tem carteira de trabalho.")
for c, k in dict.items():
    print(f"{k} é o {c}")
