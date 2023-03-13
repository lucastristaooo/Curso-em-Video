print('Calcule o seno, cosseno e tangente de um ângulo')
import math
x = float(input('Digite o ângulo que você deseja'))
a = math.sin(math.radians(x))
b = math.cos(math.radians(x))
c = math.tan(math.radians(x))
print(f'Seu seno é {a:.2f} seu cosseno é {b:.2f} e sua tangente é {c:.2f}')
