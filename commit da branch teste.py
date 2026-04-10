class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa os atributos da conta (Construtor)"""
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        """Adiciona um valor ao saldo"""
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Remove um valor do saldo, se houver o suficiente"""
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_extrato(self):
        """Mostra o status atual da conta"""
        print(f"\n--- Extrato ---")
        print(f"Titular: {self.titular}")
        print(f"Saldo atual: R${self.saldo}")
        print(f"---------------")

# --- Testando o código ---

# Criando um objeto (instância da classe)
minha_conta = ContaBancaria("Seu Nome", 100)

# Realizando operações
minha_conta.exibir_extrato()
minha_conta.depositar(50)
minha_conta.sacar(30)
minha_conta.exibir_extrato()