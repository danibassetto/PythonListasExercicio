# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

medida = float(input("Digite a distância em metros: "))
cm = medida * 100
mm = medida * 1000
print(f"A medida de {medida} m corresponde a:\n{cm} cm\n{mm} mm")