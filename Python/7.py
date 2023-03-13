print('Calcule quantos litros de tinta você precisará para pintar determinada aréa ')
l = float(input('Largura da parede'))
a = float(input('Altura da parede'))
aréa = l * a
print(f'Sua aréa tem dimensão de {l} x {a} medindo {aréa}m²')
t = aréa / 2
print(f'Você precisará de {t} litros de tinta para pintar {aréa}m²')