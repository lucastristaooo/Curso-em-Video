dict = {}
lista = []
dict["nome"] = str(input("Digite o nome do jogador: "))
partidas = int(input(f"Digite quantas partidas {dict['nome']} jogou: "))
for c in range(0, partidas):
    lista.append(int(input(f"Quantos gols {dict['nome']} marcou na partida {c+1}?")))
dict["gols"] = lista
dict["total"] = sum(lista)
print(dict) 
for c, k in dict.items():
    print(f"O campo {c} tem valor {k}")
print(f"O jogador {dict['nome']} jogou {partidas} partidas")
for c in range(0, len(lista)):
    print(f"Na partida {c+1} {dict['nome']} marcou {lista[c]} gols")
print(f"Foi um total de {dict['total']} gols")