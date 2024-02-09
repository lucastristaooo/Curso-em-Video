x = str(input("Digite uma frase: ")).strip().upper()
print(f"A letra A aparece {x.count('A')}")
print(f"A letra A aparece na primeira ocorrência: {x.find('A')}")
print(f"A letra A aparece na última ocorrência {x.rfind('A')}")