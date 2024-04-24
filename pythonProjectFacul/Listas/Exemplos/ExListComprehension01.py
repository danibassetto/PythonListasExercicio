'''
Faça um programa em python que entre com um número indefinido de nomes não compostos separados por espaço, inserindo
em uma lista por compreensão de lista, exiba a lista e após imprima o nome que tiver o menor número de caracteres
'''

print('Insira nomes separados por espaço')
nomes = input().split()
print(nomes)
tam = [len(x) for x in nomes]
menor = tam.index(min(tam))
print(nomes[menor])