print('Calcule seu IMC e veja se você está dentro da sua faixa de peso')
x = float(input('Digite seu peso (kg): '))
y = float(input('Digite sua altura (m): '))
imc = x / (y * y)
print(f'Seu IMC é de {imc:.2f}')
if imc <= 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')