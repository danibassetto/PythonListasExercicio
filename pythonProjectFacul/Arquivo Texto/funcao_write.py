'''

A função write serve para escrever valores no arquivo. A função write é um método do objeto retornado pela função open.
Dependendo da posição no arquivo, a escrita será por cima do que já estiver no arquivo.

'''

fp = open("numeros.txt","w")
for num in range(1,10):
    fp.write("{}\n".format(num))
fp.close()

'''
A função writelines serve para escrever os items de uma lista em um arquivo. 

'''

conteudo = ['a','b','c','d']
arquivo = open('texto.txt', 'w+')
arquivo.writelines(conteudo)