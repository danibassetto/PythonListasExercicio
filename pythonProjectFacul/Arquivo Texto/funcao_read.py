'''
Lê e retorna um string de caracteres ou o arquivo inteiro como um string se n não é fornecido.

Quando utilizamos a função read e executarmos a função novamente, será retornado uma string vazia.
Isso acontece porque o arquivo é como um fluxo de linhas, que começa no início do arquivo como se fosse um cursor.
Ele vai descendo e lendo o arquivo. Após ler tudo, ele fica posicionado no final do arquivo. E quando chamamos a função
read() novamente não há mais conteúdo pois ele todo já foi lido.


'''

fp = open("numeros.txt","r")
print(fp.read())
fp.close()
