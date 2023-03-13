print("Valores sorteados")
from random import randint
x = (randint(1, 10), randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10))
print(x)
for n in x:
    print(f'O maior valor sorteado foi {max(x)}')
    print(f'O menror valor sorteado foi {min(x)}')