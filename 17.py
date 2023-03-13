print('Sorteie uma ordem de alunos')
import random
a = input('Digite um nome')
b = input('Digite um nome')
c = input('Digite um nome')
d = input('Digite um último nome')
lista = a,b,c,d
r = random.choice (lista)
print(f'O aluno escolhido foi {r}')