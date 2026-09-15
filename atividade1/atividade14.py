peso = float(input("Digite o seu Peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)
if imc <= 18.5:
    print("Abaixo do peso!")
elif imc < 24.90:
    print("Peso Normal!")
elif imc < 29.00:
    print("Sobrepeso!")
elif imc > 30:
    print("Obesidade!")