valor1 = float(input('Digite o 1 valor: '))
valor2 = float(input('Digite o 2 valor: '))
while True:
    menu = int(input("""Agora, insira o número que corresponde ao que você quer fazer com seus valores
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA"""))
    soma = valor1 + valor2
    mult = valor1 * valor2
    maiorvalor = 0
    if menu == 1:
        print(f"A soma dos valores é de {soma}")
    elif menu == 2:
        print(f"A multiplicação entre os valores é de {mult}")
    elif menu == 3:
        if valor1 > valor2:
            maiorvalor = valor1
            print(f"O maior valor entre os dois inseridos é de {maiorvalor}")
        elif valor2 > valor1:
            maiorvalor = valor2
            print(f"O maior valor entre os dois inseridos é de {maiorvalor}")
        elif valor2 == valor1:
            print("Os dois valores são iguais!")
    elif menu == 4:
        print("Digite os valores novamente: ")
        valor1 = int(input("Insira o novo 1 valor: "))
        valor2 = int(input("Insira o novo 2 valor: "))
    elif menu == 5:
        print("Entendido, estamos finalizando o programa!")
        break
    else:
        print("Valor inválido!")