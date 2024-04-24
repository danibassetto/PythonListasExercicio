'''
Verificando a existência de itens em uma lista
Em alguns casos é preciso verificar se um determinado valor está contido em uma lista. Para isso, em Python
utilizamos o operador in, que indicará True se objeto pertencer ao conjunto, e False caso contrário.

'''

L = [1,2,3,4,5]
n = int(input("Informe um valor-> "))
if n in L:
    print("{} pertence a lista {}".format(n,L))
else:
    print("{} não pertence a lista {}".format(n,L))


