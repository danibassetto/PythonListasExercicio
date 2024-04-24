#Conversão de dias, horas, minutos e segundos em segundos
d=float(input("Insira o valor de dias: "))
h=float(input("Insira o valor de horas: "))
m=float(input("Insira o valor em minutos: "))
s=float(input("Insira o valor em segundos: "))
conv=(d*24*3600)+(h*3600)+(m*60)+s
print("O valor em segundos é:",conv)
