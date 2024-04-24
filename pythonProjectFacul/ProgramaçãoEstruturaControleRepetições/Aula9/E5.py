'''Elabore um algoritmo que leia as variáveis C e N, respectivamente código e número de horas trabalhadas de um operário.
E calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas excederem a 50 calcule o
excesso de pagamento armazenando-o na variável E, caso contrário zerar tal variável. A hora excedente de trabalho vale
R$ 20,00. No final do processamento imprimir o salário total e o salário excedente. '''

C = int(input("Informe o código do funcionário: "))
N = float(input(f"Insira o número de horas trabalhadas pelo operário {C}: "))

if N > 50:
    E = N - 50
    SE = E * 20
    S = 50 * 10
    ST = S + SE
    print(f"Operário {C}\nSalário: R$ {S:.2f}\nSalário Excedente: R$ {SE:.2f}\nSalário total: R$ {ST:.2f}")
else:
    E = 0
    SE = E * 20
    S = N * 10
    ST = S + SE
    print(f"Operário {C}\nSalário: R$ {S:.2f}\nSalário Excedente: R$ {SE:.2f}\nSalário total: R$ {ST:.2f}")