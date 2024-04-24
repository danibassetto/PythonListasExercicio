#Algoritmo calculo de IMC
P=float(input("Insira seu peso: "))
A=float(input("Insira sua altura: "))
IMC=P/(A**2)
if IMC<18:
    print("Indivíduo abaixo do peso")
else:
    if IMC<25:
        print("Indivíduo com peso normal")
    else:
        if IMC<30:
            print("Indivíduo acima do peso")
        else:
            print("Indivíduo obeso")
print("FIM")