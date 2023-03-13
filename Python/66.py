print("Veja tudo sobre a sua compra")
cont = preço = menor = 0
nome = ' '
while True:
    z = str(input('Digite o que você comprou: '))
    y = float(input('Digite o valor: '))
    x = str(input('Você quer continuar? SIM(S)/NÃO(N):')).upper()
    while x not in 'SN':
        x = str(input('VALOR INVÁLIDO: VOCÊ QUER CONTINUAR?')).upper()
    if y >= 1000:
        cont += 1
    if x == 'N':
        break
    if cont == 1 or preço < menor:
        menor = y
        nome = z
    resp = ' '
p = y
print('---FIM DO PROGRAMA---')
print(f'O total da compra foi de {p}')
print(f'O número de produtos custando mais de R$1000 foi {cont}')
print(f'O produto mais barato foi {nome}, custando {menor}')