# Descontos de acordo com a compra
v=float(input("Digite o valor da compra: "))
if v>=500:
    desc=v*0.25
else:
    if v>=200:
        desc=v*0.20
    else:
        desc=v*0.15
T=v-desc
print("Valor da compra R$",v)
print("Valor do desconto R$",desc)
print("Total a pagar R$",T)