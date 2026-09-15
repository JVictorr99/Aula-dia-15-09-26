idade = int(input("Digite sua Idade: "))
if idade <=0 or idade >=120:
    print("Idade Inválida")
elif idade < 12:
    print("Criança")
elif idade <= 17:
    print("Adolecente")
elif idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")

