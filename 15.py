print('Calcule um  a hipotesuna de um triangulo retangulo')
import math
co = float(input('Digite o cateto oposto'))
ca = float(input('Digite o cateto adjascente'))
h = math.hypot(ca,co)
print(f'a hipotesuna é equivalente a {h:.2f}')