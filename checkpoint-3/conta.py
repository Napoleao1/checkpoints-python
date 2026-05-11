class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.__saldo = 0.0

    def get_saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} efetuado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} autorizado.")
        else:
            print("Operação recusada! Saldo insuficiente.")

    def transferir(self, valor, conta_destino):
        if valor <= self.__saldo:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            print(f"Transferência de R$ {valor:.2f} para conta {conta_destino.numero} concluída.")
        else:
            print("Transferência recusada! Saldo insuficiente.")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def sacar(self, valor):
        super().sacar(valor + 1)


class ContaPoupanca(Conta):
    def __init__(self, numero, cliente):
        super().__init__(numero, cliente)

    def render_juros(self):
        saldo_atual = self.get_saldo()
        rendimento = saldo_atual * 0.01
        self.depositar(rendimento)
        print(f"Juros de R$ {rendimento:.2f} creditados na poupança.")
