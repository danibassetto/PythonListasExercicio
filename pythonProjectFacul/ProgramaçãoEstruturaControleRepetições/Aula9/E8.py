'''Elabore um algoritmo para calcular o valor da soma:
s = 1/2 + 1/3 + 1/4 + 1/3 + 1/4 ... 1/n
'''

n = int(input("Informe o denominador do último número a ser somado: "))

soma = 0
if n == 0:
    print("Número inválido")
else:
    for i in range(2, n+1):
        div = 1 / i
        soma += div
print(f"Soma = {soma:.3f}")