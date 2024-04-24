
xA=float(input("Digite a abscissa do ponto A: "))
yA=float(input("Digite a ordenada do ponto A: "))
xB=float(input("Digite a abscissa do ponto B: "))
yB=float(input("Digite a ordenada do ponto B: "))
DistAB=((xA-xB)**2 + (yA-yB)**2) **0.5
print(f"A distãncia entre o ponto A e B é {DistAB:.4f}")

'''rom math import sqrt

print('Entre com a coordenada do ponto 1')
x1 = float(input('x >> '))
y1 = float(input('y >> '))
print('Entre com a coordenada do ponto 2')
x2 = float(input('x >> '))
y2 = float(input('y >> '))

#dist = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
#dist = pow((x2-x1)**2 + (y2-y1)**2,(1/2))
dist = sqrt((x2-x1)**2 + (y2-y1)**2)
print(f'Distância >> {dist:.4f}')'''