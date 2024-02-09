c = 0
express = str(input("Digite uma expressão: "))
for n in express: 
    if n == "(":
        c += 1
    elif n == ")":
        c-= 1
if c % 2 == 0:
    print("Parabéns, sua expressão é válida!")
else:
    print("Sinto muito, sua expressão não foi aprovada")