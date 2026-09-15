distancia = float(input("Digite a distância em quilômetros: "))
consumo = float(input("Digite o cosumo médio do seu carro: "))
preco = float(input("Digite o preço atual da gasolina: "))
realizar = distancia / consumo
gasto = realizar * preco
print(f"Serão necessario cerca de {realizar:.2f} litros de gasolina e tera um gasto de R$ {gasto:.2f} de Combustível! ")