''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida '''

peso = float(input("Qual é seu peso?(Kg) "))
altura = float(input("Qual a sua altura?(m) "))
imc = peso / (altura ** 2)
print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    print("Indivíduo abaixo do peso")
elif imc < 25:
    print("Indivíduo com peso ideal")
elif imc < 30:
    print("Indivíduo com sobrepeso")
elif imc < 40:
    print("Indivíduo com obesidade")
else:
    print("Indivíduo com obesidade mórbida")
