'''
num1 = int(input('Digite o seu primeiro numero : '))
num2 = int(input('Digite o seu segundo numero : '))
cod = 0

centena1 = num1 // 100
dezena1 = (num1 % 100) //10
unidade1 = num1 % 10

centena2 = num2 // 100
dezena2 = (num2 % 100) //10
unidade2 = num2 % 10

if(unidade1 + unidade2) >= 10:
    cod += 1
    dezena1 += 1
if (dezena1 + dezena2) >= 10:
    cod += 1
    centena1 += 1
if(centena1 + centena2) >= 10:
    cod += 1
print('O número de vai 1 é igual a -->',cod)
'''

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

c1 = n1 // 100
d1 = n1 % 100 // 10
u1 = n1 % 100

c2 = n2 // 100
d2 = n2 % 100 // 10
u2 = n2 % 100

vai1 = 0

if u1 + u2 >= 10:
    vai1 += 1
    d1 += 1
if d1 + d2 >= 10:
    vai1 += 1
    c1 += 1
if c1 + c2 >= 10:
    vai1 += 1
    
print(f'{vai1} "vai 1"')