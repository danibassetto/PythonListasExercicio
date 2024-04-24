#algoritmo velocidade max permitida
max=float(input("Digite a velocidade máxima permitida: "))
vel=float(input("Digite a velocidade do veículo: "))
if vel>max:
    print(f"Veículo sujeito a multa por ultrapassar {vel-max} km/h")
else:
    print(f"Veículo transitando corretamente")