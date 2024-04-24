'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada Km acima do limite. '''

v = float(input("Informe a velocidade atual do carro: "))
if v > 80:
    print("MULTADO! Você excedeu o limite de 80Km/h")
    multa = (v - 80) * 7
    print(f"Valor a pagar: R${multa:.2f}")
else:
    print("Veículo trafegando dentro do limite")
