from datetime import date
x = int(input("Digite o ano de nascimento do atleta: "))
if (date.today().year-x) <= 9:
    print(f"O atleta tem {date.today().year-x} anos e se classifica como MIRIM")
elif (date.today().year-x) > 9 and (date.today().year-x) <= 14:
    print(f"O atleta tem {date.today().year-x} anos e se classifica como INFANTIL")
elif (date.today().year-x) > 14 and (date.today().year-x) <= 19:
    print(f"O atleta tem {date.today().year-x} anos e se classifica como JUNIOR")
elif (date.today().year-x) > 19 and (date.today().year-x) <= 25:
    print(f"O atleta tem {date.today().year-x} anos e se classifica como SÊNIOR")
else:
    print(f"O atleta tem {date.today().year-x} anos e se classifica como MASTER")