x = int(input("Digite a distância da viagem: "))
if x <= 200:
    print(f"O custo da viagem é de {x * 0.50}")
else:
    print(f"O custo da viagem é de {x * 0.45}")