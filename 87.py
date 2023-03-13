from random import randint
def cont(x, y):
    maior = 0
    if x > maior and x > y:
        maior = x
        a = "x"
    if y > maior and y > x:
        maior = y
        a = "y"
    print(f"O maior valor sorteado foi {maior} e estava contido em {a}")
cont(x = randint(0, 10), y = (randint(0, 10))) 
cont(x = randint(0, 100), y = (randint(0, 100)))
cont(x = randint(0, 1000), y = (randint(0, 1000)))
 