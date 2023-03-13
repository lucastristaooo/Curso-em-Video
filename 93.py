def pyhelp(*n):
        x = str(input("Digite qual função você dejesa receber ajuda: "))
        help(x)
while True: 
    pyhelp()
    x = str(input("Deseja continuar?"))
    if x == 'N':
        break
print("FIM DO PROGRAMA")