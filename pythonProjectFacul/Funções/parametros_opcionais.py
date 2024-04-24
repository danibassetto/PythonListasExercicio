'''
Parâmetros Opcionais
'''

def barra():
    print("*" * 20)
barra()

def barra(n=20, caractere="*"):
    print(caractere * n)
barra(10,"*")
barra(10)
barra(5,"&")
barra()
