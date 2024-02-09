from random import randint
n = randint(0, 5)
x = int(input("Digite um número de 0-5: "))
if x == n:
    print(f"Você venceu! Pensou no mesmo número que eu, o {n}")
else:
    print(f"Você perdeu! Eu pensei no número {n} e você no {x}")