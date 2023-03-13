print("Veja se seu nome tem 'Silva' nele")
nome = str(input('Digite seu nome completo')).strip().upper()
x = ('SILVA' in nome)
print(f'Seu nome tem Silva? {x}')