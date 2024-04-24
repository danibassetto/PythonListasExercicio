#Preço a pagar por um veiculo alugado, sendo 60 reais por dia e 0,15 centavos por km rodado
KP=float(input("Insira a quantidade de km percorrido(s): "))
QD=float(input("Insira quantos dias alugou o veículo: "))
P=(KP*0.15)+(QD*60)
print(f"O valor a ser pago pelo aluguel do veículo é {P} reais")

