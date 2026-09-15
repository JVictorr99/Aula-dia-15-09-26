valor = float(input("Digite o valor da Compra: "))

if valor <= 100:
    print("Valor sem DESCONTO!")

elif valor <= 500:
    desconto10 = valor - (valor * 0.10)
    print("Parabens você Recebeu um Desconto de 10%!")
    print("Valor Original",valor)
    print("Valor a pagar!",desconto10)

elif valor > 500:
    desconto20 = valor - (valor*0.20)
    print("Parabens Recebeu um Desconto de 20%!")
    print("Valor Original",valor)
    print("Valor a pagar!",desconto20)

