x = int(input("Digite a velocidade atual: "))
if x <= 80:
    print("Tudo ok, dirija com segurança!")
else:
    print(f"Você foi multado! O limite máximo é 80km, e você está a {x}km. Sua multa é de R${(x-80)*7}")