''' Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2 '''


larg = float(input("Insira a largura da parede: "))
alt = float(input("Insira a altura da parede: "))
a = larg * alt
print(f"Sua parede tem a dimensão de {larg} x {alt} e sua área é de {a}m")
litro = a / 2
print(f"Para pintá-la é(são) necessário(s) {litro} litro(s) de tinta")