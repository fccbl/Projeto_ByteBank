from clientes import selecionar_conta
from operacoes import ler_valor


def guardar_no_cofrinho():
    conta = selecionar_conta()
    if conta is None:
        return

    nome_caixinha = input("Nome da caixinha: ")
    valor = ler_valor("Valor a guardar: ")
    if valor is None:
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente para guardar esse valor.")
        return

    conta["saldo"] -= valor
    conta["cofrinhos"][nome_caixinha] = conta["cofrinhos"].get(nome_caixinha, 0.0) + valor
    print(f"R$ {valor:.2f} guardado na caixinha '{nome_caixinha}'.")


def resgatar_do_cofrinho():
    conta = selecionar_conta()
    if conta is None:
        return

    nome_caixinha = input("Nome da caixinha: ")
    if nome_caixinha not in conta["cofrinhos"]:
        print("Caixinha não encontrada.")
        return

    valor = ler_valor("Valor a resgatar: ")
    if valor is None:
        return

    if valor > conta["cofrinhos"][nome_caixinha]:
        print("Saldo insuficiente na caixinha.")
        return

    conta["cofrinhos"][nome_caixinha] -= valor
    conta["saldo"] += valor
    print(f"R$ {valor:.2f} resgatado da caixinha '{nome_caixinha}'.")


def simular_rendimento():
    conta = selecionar_conta()
    if conta is None:
        return

    if not conta["cofrinhos"]:
        print("Essa conta não tem caixinhas.")
        return

    taxa = 0.005
    print(f"\nSimulação de rendimento (taxa de {taxa * 100:.1f}% ao mês):")
    for nome_caixinha, valor in conta["cofrinhos"].items():
        rendimento = valor * taxa
        conta["cofrinhos"][nome_caixinha] += rendimento
        print(f"{nome_caixinha}: rendeu R$ {rendimento:.2f}, novo saldo R$ {conta['cofrinhos'][nome_caixinha]:.2f}")


def menu_cofrinhos():
    while True:
        print("\n--- Cofrinhos de Investimento ---")
        print("[1] Guardar na caixinha")
        print("[2] Resgatar da caixinha")
        print("[3] Simular rendimento")
        print("[4] Voltar")
        escolha = input("> ")

        if escolha == "1":
            guardar_no_cofrinho()
        elif escolha == "2":
            resgatar_do_cofrinho()
        elif escolha == "3":
            simular_rendimento()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
