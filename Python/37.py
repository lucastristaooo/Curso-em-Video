import math
x = float(input("Digite um número: "))
opt = int(input("Digite [1] para Binário [2] para Octal [3] para Hexadecimal: "))
if opt == 1:
    print(f"O número {x} convertido é {bin(x)}")
elif opt == 2:
    print(f"O número {x} convertido é {oct(x)}")
elif opt == 3:
    print(f"O número {x} convertido é {hex(x)}")
else:
    print("Valor inválido")