'''

A função close serve para fechar o arquivo. O fechamento garante que o sistema operacional foi informado de que não
vamos mais trabalhar com o arquivo.

'''

fp = open("numeros.txt","w")
fp.close()
