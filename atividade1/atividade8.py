n1 = float(input("Digite primeiro número: "))
n2 = float(input("Digite segundo número: "))
operacao = int(input("Digite entre as opções qual operação deseja.\n1.Soma:\n2.Subtração:\n3.multiplicação:\n4.Divisão:\n- "))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
if operacao == 1:
    print("Soma: ",soma)
elif operacao == 2:
    print("Subtração: ",sub)
elif operacao ==3:
    print("Multiplicação: ", mult)
elif operacao ==4:
    print("Divisão: ")
else:
    print("Operação inválida.")