print('Veja termos de uma fibonacci:')
x = int(input('Quantos termos você deseja ver'))
t1 = 0
t2 = 1
print(f'''{t1} 
{t2}''')
cont = 3
while cont <= x:
    t3 = t1 + t2
    print(f'{t3}')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('FIM')