from datetime import date
print('CONFIRA SEU ALISTAMENTO MILITAR')
x = int(input('Em que ano você nasceu?'))
idade = date.today().year - x
if idade == 18:
    print('Está na hora de você se alistar! Você já completou 18 anos.')
elif idade > 18:
    z = idade - 18
    print(f'Você já passou da idade de alistamento ou já se alistou a {z} ano(s).')
else:
    y = idade - 18
    print(f'Ainda faltam {y} ano(s) para você se alistar no exército!')