x = int(input("Digite o número que deseja saber o fatorial: "))
for c in range(x-1, 0, -1):
    x = x * c
print(f"O fatorial desse número é: {x}")