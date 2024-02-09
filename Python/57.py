x = str(input("Digite seu sexo [M]/[F]: ")).strip().upper()[0]
while x not in "MmFf":
    x = str(input("Digite seu sexo [M]/[F]: ")).strip().upper()[0]
print(f"Sexo {x} registrado com sucesso!")