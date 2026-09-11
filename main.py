saldo = 0.0


def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")


def ler_valor(mensagem):
    entrada = input(mensagem)
    try:
        valor = float(entrada)
    except ValueError:
        print("Valor inválido. Digite um número.")
        return None

    if valor <= 0:
        print("O valor deve ser maior que zero.")
        return None

    return valor


def depositar():
    global saldo
    valor = ler_valor("Digite o valor do depósito: ")
    if valor is None:
        return

    saldo += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")


def sacar():
    global saldo
    valor = ler_valor("Digite o valor do saque: ")
    if valor is None:
        return

    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
        return

    saldo -= valor
    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")


def exibir_menu():
    print("\n=== ByteBank MVP ===\n")
    print("[1] Consultar Saldo")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("\n> Digite a operação desejada: ")

        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            print("\nObrigado por usar o ByteBank. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
