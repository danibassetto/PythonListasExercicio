'''
Em Python, podemos ter dicionários nos quais as chaves são associadas a listas ou mesmo a outros dicionários.
Exemplo: na tabela criada anteriormente, vamos ter além do preço, a quantidade em estoque.

'''

tabela = {"Alface": [3.45,1000],
          "Batata": [3.20,500],
          "Tomate": [5.30, 2000],
          "Feijão": [4.50, 100]}
print(tabela["Alface"][0])
print(tabela["Alface"][1])

'''
Em Python, podemos ter listas onde cada cada item é um dicionário.
Exemplo: uma lista de pessoas armazenando o nome, o sexo e a idade de cada um.
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e 
todos os dicionários em uma lista. No final, mostre:
Quantas pessoas cadastradas
A média de idade
Uma lista com as mulheres
Uma lista com a idade acima da média

'''

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input("Nome: ")
    while True:
        pessoa['sexo'] = input("Sexo: [F/M] ").upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print("ERRO! Por favor, digite apenas F ou M.")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Por favor, responda apenas S ou N.")
    if resp == 'N':
        break
print("-=" * 30)
print(galera)
print("a) Ao todos temos {} pessoas cadastradas".format(len(galera)))
media = soma / len(galera)
print("b) A média de idade é de {:.2f} anos".format(media))
print("c) Mulheres cadastradas")
for p in galera:
    if p['sexo'] == 'F':
        print(p['nome'],end=" ")
print()
print("d) Lista das pessoas que estão acima da média")
for p in galera:
    if p['idade'] >= media:
        print("   ",end="")
        for k, v in p.items():
            print("{} = {}; ".format(k,v), end="")
        print()
print("<<ENCERRADO>>")

