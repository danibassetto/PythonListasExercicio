N = int(input("Quantas contas você deseja inserir? "))
conta = {}
for i in range(N):
    c = input(f"Informe o número e saldo da conta {i + 1}: ").split()
    conta[c[0]] = float(c[1])

while True:
    menu = int(input("\nInforme uma opção:"
                     "\n1. Listagem de conta e saldo"
                     "\n2. Saque"
                     "\n3. Encerrar"
                     "\n>>> "))

    if menu == 1:
        print("====== BANCO ======")
        for i in conta.items():
            print(f"Conta: {i[0]} Saldo: R${i[1]:.2f}")
