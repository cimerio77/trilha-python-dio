menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito.\n")
        deposito = int(input("Digite o valor do deposito: "))
        if deposito > 0:
            saldo += deposito
            print("Deposito efetuado com sucesso.")
            print("Saldo: R$", format(saldo, ',.2f'))
            extrato += f"Deposito: R$, {deposito:.2f}\n"
        else:
            print("Valor digitado deve ser positivo.")

    elif opcao == "s":
        print("Saque.\n\n")
        saque = int(input("Digite o valor do saque: "))
        if saque <= 500:
            if saque > saldo or numero_saques < limite_saques:
                saldo -= saque
                numero_saques += 1
                print("Saque realizado com sucesso.")
                extrato += f"Saque: R$, {saque:.2f}\n"
            else:
                print("Saldo insuficiente ou limite diário de saques ultrapassado.")
        else:
            print("O limite de cada saque é 500.")
    elif opcao == "e":
        print("Extrato.\n\n")
        print(extrato,"\n")
        print("Saldo: R$", format(saldo, ',.2f'))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
