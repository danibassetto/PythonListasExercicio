''' Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B. '''

x = input()
valores = x.split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

AT = (A * C) / 2
AC = 3.14159 * (C ** 2)
ATR = (A + B) * C / 2
AQ = B ** 2
AR = A * B

print(f"TRIANGULO: {AT:.3f}\nCIRCULO: {AC:.3f}\nTRAPEZIO: {ATR:.3f}\nQUADRADO: {AQ:.3f}\nRETANGULO: {AR:.3f}")