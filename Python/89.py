lista = []
dados = []
notas = []
media = []
while True:
    nome = str(input("Nome: ")).strip().title()
    dados.append(nome)
    n1 = float(input("Nota 1: "))
    notas.append(n1)
    n2 = float(input("Nota 2: "))
    notas.append(n2)
    media.append((n1 + n2) / 2)
    dados.append(notas[:])
    notas.clear()
    dados.append(media[:])
    media.clear()
    lista.append(dados[:])
    dados.clear()
    r = " "
    while r not in "SN":
        r = str(input("Continuar? S/N ")).strip().upper()
    if r == "N":
        break
print("~" * 30)
print("No.  NOME              MÉDIA")
print("-" * 50)
for i, n in enumerate(lista):
    print(f"{i:<5} {n[0]:<20} {n[2]}")
print("-" * 50)
while True:
    r = int(input("Mostrar notas de qual aluno? (999 Interrompe): "))
    if r == 999:
        break
    else:
        for i, p in enumerate(lista):
            if i == r:
                print(f"Notas de {p[0]} são {p[1]}")
print("Programa finalizado!")