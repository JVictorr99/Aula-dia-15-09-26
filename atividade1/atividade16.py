print("Ordem de saque")
valor = int(input("Digite o valor que desaja sacar: \033[1;33m"))
print("\033[m")

if valor <= 0:
    print("Valor invalido!")
else:
    nota100 = valor // 100
    valor = valor % 100
    
    nota50 = valor // 50
    valor = valor % 50
    
    nota20 = valor // 20
    valor = valor % 20
    
    nota10 = valor // 10
    valor = valor % 10
    
    if valor != 0:
        print("Não é possível formar esse valor com as Notas Disponíveis ")
    
    else:
        print(f"{nota100} Nota(s) de R$100")
        print(f"{nota50} Nota(s) de R$50")
        print(f"{nota20} Nota(s) de RR$20")
        print(f"{nota10} Nota(s) de R$10")
