def votação(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        print(f"Com {idade} anos ainda não se vota")
    elif 16 <= idade < 18 or idade > 65:
        print(f"Com {idade} anos o voto é opcinal")
    else:
        print(f"Com {idade} anos o voto é obrigatório")
votação(2003)