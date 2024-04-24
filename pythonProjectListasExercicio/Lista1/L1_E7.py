#Gasto de litros e dinheiro entre duas cidades
P=float(input("Insira o preço do combustível: "))
D=float(input("Insira o desempenho em km/l que o veículo apresenta: "))
Dist=float(input("Insira a distância em km entre as duas cidades: "))
Consumo_de_Combustivel=Dist/D
Dinheiro_Gasto=P*Consumo_de_Combustivel
print(f"Para andar {Dist}km você irá consumir {Consumo_de_Combustivel:.2f} litros e gastará {Dinheiro_Gasto:.2f} reais")

