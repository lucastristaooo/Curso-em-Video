n1 = float(input("Digite sua priimeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
if 7 > (n1+n2)/2 > 5:
    print("Aluno de RECUPERAÇÃO")
elif (n1+n2)/2 >= 7:
    print("Aluno APROVADO")
elif (n1+n2)/2 < 5:
    print("aluno REPROVADO")