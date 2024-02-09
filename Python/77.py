lista = ["AMOR", "COMER", "ANDAR", "CORRER", "MASTIGAR"]
palavras = []
vogais = {}
for palavra in lista:
    print(f"\n Na palavra {palavra} temos", end=" ")
    for letra in palavra:
        if letra.upper() in "AEIOU":
            print(f"{letra}", end=" ")
