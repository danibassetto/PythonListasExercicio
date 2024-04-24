'''
Retorna a próxima linha do arquivo com todo o texto e incluindo o caractere de nova linha. Se é fornecido como argumento
 então somente n caracteres são retornados se a linha tem mais do que n caracteres.
'''

fp = open("numeros.txt","r")
print(fp.readline())
fp.close()

fp = open("numeros.txt","r")
for n in fp:
    print(n)
fp.close()

fp = open('numeros.txt', 'r')
numeros = []
for num in fp:
    num = num.strip()
numeros.append(num)
print(numeros)
fp.close()

'''
Readlines
Retorna uma lista de strings, cada um representado o conteúdo de uma linha do arquivo. Se n não é fornecido, todas as 
linhas do arquivo são retornadas. Se n é fornecido como argumento então n caracteres serão lidos mas n é arrendondado 
para cima de tal forma que uma linha inteira seja retornada.
'''

fp = open("numeros.txt","r")
print(fp.readlines())
fp.close()


