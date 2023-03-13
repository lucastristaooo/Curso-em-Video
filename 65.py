cont18 = 0
contsub18 = 0
contsexo = 0
while True:
    print('CADESTRE UMA PESSOA')
    x = int(input('Digite a idade: '))
    y = str(input('Digite o sexo (M/F): ')).upper()
    p = str(input('Quer continuar? (S/N)')).upper()
    if x >= 18:
        cont18 = cont18 + 1
    if x <= 20 and y == 'F':
        contsub18 = contsub18 + 1
    if y == 'M':
        contsexo += 1
    if p != 'S':
        break
    print('CONTINUANDO...')
print(f'''PROGRAMA FINALIZADO
Total de pessoas com mais de 18 anos: {cont18}
Ao todos temos {contsexo} homens cadastrados
E temos {contsub18} mulheres com menos de 20 anos''')