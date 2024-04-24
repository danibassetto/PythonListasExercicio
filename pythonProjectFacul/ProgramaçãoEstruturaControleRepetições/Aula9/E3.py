'''Elabore um algoritmo que leia a idade de uma pessoa e defina se ela pode votar (idade>= 16), se ela pode dirigir
(idade >=18) ou se pode ambos, votar e dirigir.
'''

idade = int(input("Informe a sua idade: "))

if idade < 0:
    print("Idade inválida!")
elif idade < 16:
    print("Você não pode votar e nem dirigir!")
elif idade >= 16 and idade < 18:
    print("Você pode votar, mas não pode dirigir!")
else:
    print("Você pode votar e dirigir!")