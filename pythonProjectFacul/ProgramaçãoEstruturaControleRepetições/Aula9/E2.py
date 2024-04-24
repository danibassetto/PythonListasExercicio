''' Elabore um algoritmo que leia a velocidade máxima permitida em uma estrada e também a velocidade que um determinado
veículo trafega. Verifique se o veículo está dentro da velocidade permitida ou acima dela. Caso esteja acima,
quanto está acima? '''

v = int(input("Informe a velocidade máxima permitida na estrada [Km/h]: "))
V = int(input("Informe a velocidade do veículo [Km/h]: "))

if V <= v:
    print("Veículo trafegando na velocidade correta!")
else:
    acima = V - v
    print(f"O veículo está {acima} Km/h acima da velocidade permitida!")

