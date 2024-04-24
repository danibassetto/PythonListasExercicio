'''
A instrução del é utilizada para remover elementos do dicionário.
'''

tabela = {"Alface": 3.45,
          "Batata": 3.20,
          "Tomate": 5.30,
          "Feijão": 4.50}
print(tabela)
del tabela ["Tomate"]
print(tabela)

'''
O método pop(), além de remover o elemento com a chave especificada do dicionário, nos retorna o valor desse 
elemento. Também podemos definir um valor padrão de retorno, para caso a chave não seja encontrada.
'''
tabela = {"Alface": 3.45,
          "Batata": 3.20,
          "Tomate": 5.30,
          "Feijão": 4.50}
print(tabela.pop("Alface","Não consta na lista"))
print(tabela.pop("Cenoura","Não consta na lista"))
