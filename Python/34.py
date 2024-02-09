x = float(input("Digite o salário: "))
if x >= 1250:
    print(f"O novo salário é de: R${x+(x*0.10)}")
else:
    print(f"O novo salário é de: R${x+(x*0.15)}")