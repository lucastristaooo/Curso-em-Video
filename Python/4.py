x = str(input("Digite uma frase: "))
print(f"O tipo primitivo é {type(x)}")
print(f"Só tem espaços? {x.isspace()}")
print(f"É número? {x.isdigit()}")
print(f"É alfabético? {x.isalpha()}")
print(f"É alfanúmerico? {x.isalnum()}")
print(f"Está em maiúsculas? {x.isupper()}")
print(f"Está em minúsculas? {x.islower()}")
print(f"Está em capitalizada? {x.istitle()}")
