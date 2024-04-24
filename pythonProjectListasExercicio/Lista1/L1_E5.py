#Troca de variáveis A e B
A=float(input("Insira um número: "))
B=float(input("Insira outro número: "))
print(f"Antes da troca: \nA={A}\nB={B}")
C=A
A=B
B=C
print(f"Após a troca: \nA={A}\nB={B}")
#no python também poderia por a,b=b,a