def cont(x,y,z):
    for c in range(x,y,z):
        print(c)        
    print("=" * 5)
print(f"DE 1 EM 1") 
cont(x=1, y= 10, z = 1)
print(f"DE 2 EM 2")
cont(x=0, y= 10, z = 2)
print(f"AGORA É COM VOCÊ")
cont(x = int(input("Começo: ")), y = int(input("Fim: ")), z = int(input("Passo: ")))