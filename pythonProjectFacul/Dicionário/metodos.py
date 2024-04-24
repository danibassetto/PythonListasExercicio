'''
Método get()
O método get() tenta obter a chave procurada; caso não a encontre, retorna o segundo parâmetro. Se o segundo parâmetro
não for especificado, get retornará None. Quando a chave é encontrada no dicionário, get retorna o valor atualmente
associado.
'''

tabela = {"Alface": 3.45,
          "Batata": 3.20,
          "Tomate": 5.30,
          "Feijão": 4.50}
print(tabela.get("Alface","Não consta na lista"))
print(tabela.get("Cenoura","Não consta na lista"))

'''
Métodos key() e values()
Podemos obter uma lista com as chaves do dicionário, ou mesmo uma lista dos valores associados.

'''

print(tabela.keys())
print(tabela.values())
