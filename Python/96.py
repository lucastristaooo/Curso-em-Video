def área(largura, comprimento):
    área = largura * comprimento
    return área
largura = float(input("Digite a largura (m): "))
comprimento = float(input("Digite o comprimento (m): "))
soma = (área(largura, comprimento))
print(f"A área do terreno é de {largura}m x {comprimento}m = {soma} metros quadradados")