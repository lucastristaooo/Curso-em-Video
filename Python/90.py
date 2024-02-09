dict = {}
dict["nome"] = str(input("Digite o nom: "))
dict["nota"] = int(input(f"Digite a nota de {dict['nome']}"))
if dict["nota"] >= 7:
    dict["situação"] = "Aprovado"
elif 5 <= dict["nota"] < 7:
    dict["situação"] = "Recuperação"
else:
    dict["situação"] = "Reprovado"
for k, v in dict.items():
    print(f"{k} é igual a {v}")