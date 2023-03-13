print("Digite seu sexo")
p = str(input('Digite um sexo (M/F): ')).upper()
while p not in ('MmFF'):
    p = str(input('Digite um sexo (M/F): ')).upper()
print(f'Sucesso! o sexo foi {p}')