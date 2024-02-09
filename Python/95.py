dict = {}
lista = []
gols = []
while True:
    dict["nome"] = str(input(("Digite o nome do jogador: ")))
    dict["partidas"] = int(input(f"Quantas partidas {dict['nome']} jogou?"))
    for c in range(0, dict["partidas"]):
        gols.append(int(input(f"Quantos gols {dict['nome']} marcou na partida {c+1}")))
    dict["gols"] = gols[:]
    gols.clear()
    lista.append(dict.copy())
    continuar = str(input("Deseja continuar? (S/N)")).strip().upper()
    if continuar not in "SN":
        continuar = str(input("Deseja continuar? (S/N)"))
    if continuar == "N":
        break
for c in lista:
        print(c)
while True:
    dados = int(input("Deseja mostrar dados de qual jogador? (999 - Sair)"))
    if dados == 999:
        break
    if dados >= len(lista):
        print("Erro! Não existe esse jogador na lista")
    else:
        for i, g in enumerate(lista[dados]["gols"]):
                print(f"Na partida {i+1} marcou {g} gols")