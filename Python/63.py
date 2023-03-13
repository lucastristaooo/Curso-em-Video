while True:
    x = int(input('Quer ver a tabuada de qual valor? [NÚMERO NEGATIVO PARA FINALIZAR]: '))
    if x < 0:
        break
    else:       
        for c in range(1, 11):
            p = x * c
            print(f'{x} x {c} = {p}')
print('PROGRAMA FINALIZADO COM SUCESSO')