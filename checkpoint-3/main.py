from cliente import Cliente
from conta import ContaCorrente


def main():
    cliente = Cliente("Ernani", "123.456.789-00")
    conta = ContaCorrente(1, cliente)

    while True:
        print("\n===== CAIXA ELETRÔNICO =====")
        print(f"Cliente: {conta.cliente.nome}")
        print("[1] Ver Saldo")
        print("[2] Depositar")
        print("[3] Sacar")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                print(f"Saldo atual: R$ {conta.get_saldo():.2f}")
            case "2":
                valor = float(input("Valor do depósito: R$ "))
                conta.depositar(valor)
            case "3":
                valor = float(input("Valor do saque: R$ "))
                conta.sacar(valor)
            case "4":
                print("Encerrando... Até a próxima!")
                break
            case _:
                print("Opção inválida.")


if __name__ == "__main__":
    main()
