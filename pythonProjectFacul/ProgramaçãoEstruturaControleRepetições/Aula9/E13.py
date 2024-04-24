'''Uma empresa de cosméticos irá lançar um novo produto no mercado. Para saber se haverá aceitação,
produziu 2000 amostras e as distribuiu a uma população. Cada pessoa respondeu se gostou ou não do produto (‘s’ ou ‘n’)
e o seu sexo (‘f’ ou ‘m’). Elabore um algoritmo para:

a)Calcular o total de homens e o total de mulheres que gostaram do produto.
b)Calcular o total de homens e o total de mulheres que não gostaram do produto.
c)A empresa deve ou não lançar o produto?

'''
nao_gostaram = 0
gostaram = 0
feminino = 0
masculino = 0

for i in range(1, 5):
    aceitacao = input("Informe se gostou ou não do produto [S/N]: ").upper()
    sexo = input("Informe seu sexo [F/M]: ").upper()
    if aceitacao == 'N':
        nao_gostaram += 1
    elif aceitacao == 'S':
        gostaram += 1
    if sexo == 'F':
        feminino += 1
    elif sexo == 'M':
        masculino += 1
print("-" * 50)
print(f"Pessoas que não gostaram: {nao_gostaram}\nPessoas que gostaram: {gostaram}\nQuantidade de mulheres "
      f"que participaram: {feminino}\nQuantidade de homens que participaram: {masculino}")
if gostaram > nao_gostaram:
    print("PRODUTO ACEITO!")
else:
    print("PRODUTO MAL ACEITO!")
