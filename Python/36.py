vc = float(input("Digite o valor da casa: "))
sal = float(input("Digite o seu salário: "))
prestação = int(input("Digite em quantos anos deseja pagar a casa: "))
tempo = vc / (prestação * 12)
if tempo > (sal*0.3):
    print("Empréstimo negado")
else:
    print("Empréstimo aceito")