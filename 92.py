def nota(*n,):
    dict = {}
    dict['total'] = len(n)
    dict['maior'] = max(n)
    dict['menor'] = min(n)
    dict['media'] = sum(n) / len(n)
    if dict['media'] >= 7:
        dict['sit'] = 'BOA'
    elif dict['media'] <=6:
        dict['sit'] = 'RUIM'
    return dict
resp = int(input("Digite as notas: "))
resp2 = int(input("Digite a segunda nota: "))
resp3 = int(input("Digite a terceira nota: "))
nota(resp, resp2, resp3)