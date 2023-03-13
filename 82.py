dict = {}
gols = []
dict['nome'] = str(input("Digite o nome do jogador: "))
dict['partidas'] = int(input(f"Quantas partidas {dict['nome']} jogou?"))
dict['gols'] = gols
for c in range(dict['partidas']):
    gols.append(int(input(f"Quantos gols {dict['nome']} marcou na partida {c+1}?")))
dict['total'] = sum(gols)
print(dict)
print()
for k, v in dict.items():
    print(f"{k} tem o valor {v}")
print()
print(f"O jogador {dict['nome']} jogou {dict['partidas']} partidas")
for i, v in enumerate(dict['gols']):
    print(f"Na partida {i+1} ele fez {v} gols")