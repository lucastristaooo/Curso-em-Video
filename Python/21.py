print("Veja o preço do aluguel de um carro")
x = float(input('Quantos km ele andou?'))
x1 = float(input('Quantos dias você ficou com ele?'))
x2 = x * 60
x3 = x1 * 0.15
x4 = x2 + x3
print(f'O valor total a pagar é de {x4}R$')