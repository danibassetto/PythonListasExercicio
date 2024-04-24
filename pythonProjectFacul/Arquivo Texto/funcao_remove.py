'''
A função remove apaga o arquivo na pasta especifica, se o mesmo existir.
'''


import os
if os.path.exists("numeros.txt"):
    os.remove("numeros.txt")
else:
    print("O arquivo não existe!")
