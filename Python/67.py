while True:
    x = int(input("Digite um número: "))
    for c in range(1, 11):
        print(f"{x} x {c} = {x*c}")
    if x < 0:
        break
print("FIM DO PROGRAMA")