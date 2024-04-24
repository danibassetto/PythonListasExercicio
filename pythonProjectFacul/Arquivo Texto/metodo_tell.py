'''
O método tell() devolve um inteiro long que indica a posição atual de leitura ou escrita no arquivo,
medida em bytes desde o início do arquivo.

'''

f = open('teste.txt', 'a+')
f.write('0123456789abcdef')
f.seek(5)     # Vai para o sexto byte do arquivo
print(f.read(1))
print(f.tell())
