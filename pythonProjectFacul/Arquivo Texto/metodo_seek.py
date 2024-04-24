'''
Posiciona o cursor em um ponto do arquivo: seek (colunas, posição). A posição 0 é o início do arquivo, 1 usa a posição
do arquivo atual e 2 usa o final do arquivo como ponto de referência. Se a posição é omitida o padrão é 0.

'''

fp = open("numeros.txt","r")
print('Números')
print(fp.read())
print("Mostrando novamente os números")
fp.seek(0)
print(fp.read())
fp.close()
