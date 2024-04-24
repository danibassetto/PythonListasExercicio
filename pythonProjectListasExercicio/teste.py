placa = input("Digite a placa: ").upper()

if len(placa) != 7 or not placa[5:7].isnumeric() or placa[:3].isnumeric():
    print("Formato inválido")
else:
    if placa[0].isdigit(): # Padrão Brasil
        placa_mercosul = placa[:3] + placa[3:].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D').replace('4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I').replace('9', 'J')
        print(f"Padrão: Brasil\nCorrespondente: {placa_mercosul}")
    else: # Padrão Mercosul
        placa_brasil = placa[:3] + placa[3:].replace('A', '0').replace('B', '1').replace('C', '2').replace('D', '3').replace('E', '4').replace('F', '5').replace('G', '6').replace('H', '7').replace('I', '8').replace('J', '9')
        print(f"Padrão: Mercosul\nCorrespondente: {placa_brasil}")