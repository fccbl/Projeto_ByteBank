from clientes import selecionar_conta
from operacoes import ler_valor


def ler_numero_parcelas():
    parcelas_str = input("Número de parcelas: ")
    try:
        parcelas = int(parcelas_str)
    except ValueError:
        print("Número de parcelas inválido.")
        return None

    if parcelas <= 0:
        print("O número de parcelas deve ser maior que zero.")
        return None

    return parcelas


def simular_emprestimo():
    conta = selecionar_conta()
    if conta is None:
        return

    limite = conta["saldo"] * 3
    print(f"\nLimite de empréstimo disponível: R$ {limite:.2f}")

    valor = ler_valor("Valor desejado para simular: ")
    if valor is None:
        return

    if valor > limite:
        print("Valor acima do limite disponível.")
        return

    parcelas = ler_numero_parcelas()
    if parcelas is None:
        return

    valor_parcela = valor / parcelas
    print(f"Simulação: {parcelas}x de R$ {valor_parcela:.2f}")


def contratar_emprestimo():
    conta = selecionar_conta()
    if conta is None:
        return

    limite = conta["saldo"] * 3
    valor = ler_valor("Valor do empréstimo: ")
    if valor is None:
        return

    if valor > limite:
        print("Valor acima do limite disponível (3x o saldo atual).")
        return

    parcelas = ler_numero_parcelas()
    if parcelas is None:
        return

    valor_parcela = valor / parcelas
    conta["saldo"] += valor
    conta["emprestimos"].append(
        {
            "valor_total": valor,
            "parcelas": parcelas,
            "valor_parcela": valor_parcela,
            "parcelas_pagas": 0,
        }
    )
    print(f"Empréstimo de R$ {valor:.2f} aprovado em {parcelas}x de R$ {valor_parcela:.2f}.")


def pagar_parcela_emprestimo():
    conta = selecionar_conta()
    if conta is None:
        return

    emprestimos_ativos = [e for e in conta["emprestimos"] if e["parcelas_pagas"] < e["parcelas"]]
    if not emprestimos_ativos:
        print("Não há empréstimos com parcelas pendentes.")
        return

    emprestimo = emprestimos_ativos[0]
    valor_parcela = emprestimo["valor_parcela"]
    if valor_parcela > conta["saldo"]:
        print("Saldo insuficiente para pagar a parcela.")
        return

    conta["saldo"] -= valor_parcela
    emprestimo["parcelas_pagas"] += 1
    restantes = emprestimo["parcelas"] - emprestimo["parcelas_pagas"]
    print(f"Parcela de R$ {valor_parcela:.2f} paga. Restam {restantes} parcela(s).")


def menu_emprestimos():
    while True:
        print("\n--- Empréstimos ---")
        print("[1] Simular empréstimo")
        print("[2] Contratar empréstimo")
        print("[3] Pagar parcela")
        print("[4] Voltar")
        escolha = input("> ")

        if escolha == "1":
            simular_emprestimo()
        elif escolha == "2":
            contratar_emprestimo()
        elif escolha == "3":
            pagar_parcela_emprestimo()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
