'''
Tuplas --> representadas entre () e seus objetos são imutáveis e podem ter dados de tipos diferentes

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata frita"))

for comida in lanche:
	print(f"Vou comer {comida}")

for cont in range(0, len(lanche)):
	print(f"Vou comer {lanche[cont]} na posição {cont}")

for pos, comida in enumerate(lanche):
	print(f"Vou comer {comida} na posição {pos}")

print(sorted(lanche)) # ordenando uma tupla


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # cola uma na outra
print(c)

print(len(c))  # Diz o tamanho
print(c.count(2))  # mostra quantas vezes o 2 aparece em c
print(c.index(2))  # mostra a primeira posição do 2 em c
print(c.index(2, 4))  # mostra a primeira posiçaõ do 2 a partir da posição 3
'''
