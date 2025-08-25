from abc import ABC, abstractmethod


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, numero, agencia, cliente, saldo=0, historico=None):
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._saldo = saldo
        self._historico = historico or Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def historico(self):
        return self._historico

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente.")
            return False
        self._saldo -= valor
        self._historico.adicionar_transacao(f"Saque: R$ {valor:.2f}")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
            return False
        self._saldo += valor
        self._historico.adicionar_transacao(f"Depósito: R$ {valor:.2f}")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, '0001', cliente, saldo=0, historico=Historico())
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        sucesso = transacao.registrar(conta)
        if sucesso:
            print("Transação realizada com sucesso.")
        else:
            print("Falha na transação.")

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)



def apresentar_extrato(conta):
    print("\n=== Extrato ===")
    for transacao in conta.historico.transacoes:
        print(transacao)
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}\n")

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace('.', '').replace('-', '')
    return PessoaFisica(nome, data_nascimento, cpf, endereco)

def criar_conta(cliente, numero_conta):
    conta = ContaCorrente(numero_conta, cliente)
    cliente.adicionar_conta(conta)
    return conta


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair
=> """

usuarios = []
contas = []
numero_conta = 1

while True:
    opcao = input(menu)

    if opcao == "u":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")
        usuario = criar_usuario(nome, data_nascimento, cpf, endereco)
        usuarios.append(usuario)
        print(f"Usuário {nome} criado com sucesso.\n")

    elif opcao == "c":
        cpf = input("Informe o CPF do usuário: ").replace('.', '').replace('-', '')
        cliente = next((u for u in usuarios if u.cpf == cpf), None)
        if cliente:
            conta = criar_conta(cliente, numero_conta)
            contas.append(conta)
            numero_conta += 1
            print(f"Conta criada com sucesso para {cliente.nome}.\n")
        else:
            print("Usuário não encontrado.\n")

    elif opcao == "d":
        cpf = input("CPF do titular: ").replace('.', '').replace('-', '')
        cliente = next((u for u in usuarios if u.cpf == cpf), None)
        if cliente and cliente.contas:
            valor = float(input("Valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)
        else:
            print("Cliente ou conta não encontrada.\n")

    elif opcao == "s":
        cpf = input("CPF do titular: ").replace('.', '').replace('-', '')
        cliente = next((u for u in usuarios if u.cpf == cpf), None)
        if cliente and cliente.contas:
            valor = float(input("Valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)
        else:
            print("Cliente ou conta não encontrada.\n")

    elif opcao == "e":
        cpf = input("CPF do titular: ").replace('.', '').replace('-', '')
        cliente = next((u for u in usuarios if u.cpf == cpf), None)
        if cliente and cliente.contas:
            apresentar_extrato(cliente.contas[0])
        else:
            print("Cliente ou conta não encontrada.\n")

    elif opcao == "q":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.\n")
