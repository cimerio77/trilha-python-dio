menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[u] Criar Usuario
[c] Criar Conta

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3
numero_conta = 1
usuarios = []
contas = []



def deposito(saldo, valor, extrato):
    saldo += valor
    extrato += f'Deposito: R$ {valor:.2f}\n'
    return saldo, extrato

def sacar(saldo, valor, extrato):
    saldo -= valor
    extrato += f'Saque: R$ {valor:.2f}\n'
    return saldo, extrato

def apresentar_extrato(saldo, extrato):
    print("Extrato.\n")
    print(extrato, "\n")
    print("Saldo: R$", format(saldo, ',.2f'))

def cria_usuario(nome, data_nascimento, cpf, endereco):
    print("Novo usuario.\n")
    usuario = []
    cpf = cpf.replace('.', '').replace('-', '')
    usuario.append(cpf)
    usuario.append(nome)
    usuario.append(data_nascimento)
    usuario.append(endereco)
    return usuario

def cria_conta(usuario):
    print("Nova conta.\n")
    global numero_conta
    agencia = '0001'
    nova_conta = [numero_conta, agencia, usuario]
    numero_conta += 1
    return nova_conta

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito.\n")
        valor = int(input("Digite o valor do deposito: "))
        if valor > 0:
            saldo, extrato = deposito(saldo, valor, extrato)
            print("Deposito efetuado com sucesso.")
            print("Saldo: R$", format(saldo, ',.2f'))
        else:
            print("Valor digitado deve ser positivo.")

    elif opcao == "s":
        print("Saque.\n")
        valor = int(input("Digite o valor do saque: "))
        if valor <= 500:
            if valor <= saldo and numero_saques <= limite_saques:
                saldo, extrato = sacar(saldo, valor, extrato)
                print("Saque realizado com sucesso.")
                print("Saldo: R$", format(saldo, ',.2f'))
                numero_saques += 1
            else:
                print("Saldo insuficiente ou limite diário de saques ultrapassado.")
        else:
            print("O limite de cada saque é 500.")
    elif opcao == "e":
        apresentar_extrato(saldo, extrato)

    elif opcao == "u":
        usuario1 = cria_usuario('paulo', '30/01/1979', '86878707820', 'qn 12d conjunto 1')
        usuario2 = cria_usuario('fernanda', '10/05/1993', '79760787803', 'rua andre 18')
        usuarios.append(usuario1)
        usuarios.append(usuario2)

    elif opcao == "c":
        for usuario in usuarios:
            nova_conta = cria_conta(usuario)
            contas.append(nova_conta)
            print(f"Conta criada com sucesso para {usuario[1]} (CPF: {usuario[0]})")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
