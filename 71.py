palavras = ('Sagui', 'Melão', 'Coração', 'Motel', 'Chalita')
for l in palavras:
    print(f'Na palavra {l} temos as vogais:')
    for letra in l:
        if letra.lower() in 'a, ã, e, ê, e, i, i, õ, o, u':
            print(f'{letra}')