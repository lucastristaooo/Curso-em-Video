def voto(anodenascimento):
    if anodenascimento >= 16 and anodenascimento <= 17 or anodenascimento > 65:
        return f"SEU VOTO É OPCIONAL"
    elif anodenascimento >= 18:
        return f"SEU VOTO É OBRIGATÓRIO"
    elif anodenascimento < 16:
        return f"SEU VOTO NÃO PODE SER COTADO"
ano = int(input("Digite sua idade: "))
x = print(voto(ano))