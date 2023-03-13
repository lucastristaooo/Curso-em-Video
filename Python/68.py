print("Veja a ordem de 0 a 20")
p = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f'{p[1:6]}')
print(f'{p[17:21]}')
print(f'{sorted(p)}')
print(f'{p.index("nove")}')