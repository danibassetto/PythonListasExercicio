'''  Elabore um algoritmo, usando a estrutura PARA, que leia um número inteiro e calcule o seu fatorial. Ex. o fatorial de
n==5 é 120, pois: 5! = 5*4*3*2*1== 120. '''

n = int(input("Insira o número que deseja saber o fatorial: "))
fat = 1
for i in range(n, 1, -1):
    fat *= i
print(f"Fatorial de {n} = {fat}")
