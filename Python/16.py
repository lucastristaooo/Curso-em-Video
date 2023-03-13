print('Sorteie um aluno')
import random
a = input('Digite um nome')
b = input('Digite um nome')
c = input('Digite um nome')
d = input('Digite um último nome')
lista = [a,b,c,d]
random.shuffle(lista)
r = lista
print(f'O aluno escolhido foi {r}')