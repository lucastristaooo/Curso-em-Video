x = str(input('Deseja começar? Sim(S)/Não(N): ')).strip().upper()
a = []
if x == 'S':
    while True:
        y = int(input('Digite um número: '))
        if y not in a:
            a.append(y)
            print('Valor adicionado com sucesso!')
        else:
            print('Valor já foi adicionado uma vez, não irei repeti-lo')
        x = str(input('Deseja continuar? Sim(S)/Não(N): ')).strip().upper()
        if x != 'S':
            break
    a.sort()
    print(f'Os número digitados foram: {a}')
else:
    print('FIM DO PROGRAMA')