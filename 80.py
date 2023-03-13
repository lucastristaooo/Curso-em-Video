dic = {}
dic['nome'] = str(input("Digite um nome: "))
dic['média'] = float(input("Digite a média: "))
print(f"Seu nome é: {dic['nome']}")
print(f"Sua média é: {dic['média']}")
if dic['média'] >= 7:
    print(f"Situação: Aprovado")
elif dic['média'] >= 5:
    print(f"Situação: Recuperação")
elif dic['média'] < 4:
    print(f"Situação: Reprovado")