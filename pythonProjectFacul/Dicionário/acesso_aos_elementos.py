'''
Um dicionário é acessado por suas chaves. Diferentemente de listas, em que o índice é um número, dicionários utilizam
suas chaves como índice. Quando atribuímos um valor a uma chave, duas coisas podem ocorrer:
	1. Se a chave já existe: o valor associado é alterado para o novo valor.
	2. Se a chave não existe: a nova chave será adicionado ao dicionário.
'''

tabela = {"Alface": 3.45,
          "Batata": 3.20,
          "Tomate": 5.30,
          "Feijão": 4.50}
print(tabela)
print(tabela["Alface"])
tabela["Tomate"] = 5.50
tabela["Cebola"] = 4.68
print(tabela)

'''
Para o acesso aos dados, temos que verificar se uma chave existe, antes de acessá-la. Para isso, podemos usar o operador
in.
'''

if "Manga" in tabela:
    print(tabela["Manga"])
else:
    print("Não há Manga")

