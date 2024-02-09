def enumero(num):
    while True:
        valor = input(num)
        if valor.isnumeric():
            return(int(valor))
        else:
            print(f"O digito {valor} não é um número")
resposta = enumero("Digite um número: ")
print(f"O número digitado foi valor {resposta}")