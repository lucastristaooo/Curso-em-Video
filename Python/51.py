from datetime import date
print("Veja quem são as pessoas maiores de idade")
atual = date.today().year
a = 0
b = 0
for c in range (1,8):
    x = int(input('Digite o ano de nascimento:'))
    y = atual - x
    if y >= 18:
        a+=1
    else:
        b+=1
print(f'{a} pessoas são maiores de idade')
print(f'{b} pessoas sao menores de idade')