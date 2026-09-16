contas = [
    {"nome": "Ana Clara Fornellos", "chave_pix": "ana@bytebank", "saldo": 500.0},
    {"nome": "Fabiana Lima", "chave_pix": "fabiana@bytebank", "saldo": 300.0},
    {"nome": "Cliente Teste", "chave_pix": "teste@bytebank", "saldo": 1000.0},
]


def buscar_conta(chave_pix):
    for conta in contas:
        if conta["chave_pix"] == chave_pix:
            return conta
    return None


def selecionar_conta():
    chave = input("Digite a chave PIX da conta: ")
    conta = buscar_conta(chave)
    if conta is None:
        print("Conta não encontrada.")
    return conta


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


def consultar_saldo():
    conta = selecionar_conta()
    if conta is None:
        return

    print(f"\nSaldo de {conta['nome']}: R$ {conta['saldo']:.2f}")


def depositar():
    conta = selecionar_conta()
    if conta is None:
        return

    valor = ler_valor("Digite o valor do depósito: ")
    if valor is None:
        return

    conta["saldo"] += valor
    print(f"Depósito de R$ {valor:.2f} realizado com sucesso para {conta['nome']}.")


def sacar():
    conta = selecionar_conta()
    if conta is None:
        return

    valor = ler_valor("Digite o valor do saque: ")
    if valor is None:
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente para realizar o saque.")
        return

    conta["saldo"] -= valor
    print(f"Saque de R$ {valor:.2f} realizado com sucesso de {conta['nome']}.")


def transferir():
    chave_origem = input("Digite a chave PIX da conta de origem: ")
    conta_origem = buscar_conta(chave_origem)
    if conta_origem is None:
        print("Conta de origem não encontrada.")
        return

    chave_destino = input("Digite a chave PIX da conta de destino: ")
    conta_destino = buscar_conta(chave_destino)
    if conta_destino is None:
        print("Conta de destino não encontrada.")
        return

    if conta_origem is conta_destino:
        print("Não é possível transferir para a mesma conta.")
        return

    valor = ler_valor("Digite o valor da transferência: ")
    if valor is None:
        return

    if valor > conta_origem["saldo"]:
        print("Saldo insuficiente para realizar a transferência.")
        return

    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor
    print(
        f"Transferência de R$ {valor:.2f} de {conta_origem['nome']} "
        f"para {conta_destino['nome']} realizada com sucesso."
    )


def exibir_menu():
    print("\n=== ByteBank MVP ===\n")
    print("[1] Consultar Saldo")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Transferir (PIX)")
    print("[5] Sair")


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
            transferir()
        elif opcao == "5":
            print("\nObrigado por usar o ByteBank. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
