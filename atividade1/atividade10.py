n1 = int(input("Primeiro Número: "))
n2 = int(input("Segundo Número: "))
n3 = int(input("Terceiro Número: "))

if n1 > n2 and n1 > n3:
    Maior = n1
elif n2 > n1 and n2 > n3:
    Maior = n2
else:
    Maior = n3


if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
    
print("Maior", Maior)
print("menor", menor)