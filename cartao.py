from clientes import selecionar_conta
from operacoes import ler_valor, registrar_historico


def comprar_no_credito():
    conta = selecionar_conta()
    if conta is None:
        return

    estabelecimento = input("Nome do estabelecimento: ")
    valor = ler_valor("Valor da compra: ")
    if valor is None:
        return

    limite_disponivel = conta["limite_credito"] - conta["saldo_fatura"]
    if valor > limite_disponivel:
        print("Limite de crédito insuficiente.")
        return

    conta["saldo_fatura"] += valor
    registrar_historico(conta, "Compra no Crédito", valor, detalhes={"estabelecimento": estabelecimento})
    print(f"Compra de R$ {valor:.2f} em {estabelecimento} lançada na fatura.")


def pagar_fatura():
    conta = selecionar_conta()
    if conta is None:
        return

    if conta["saldo_fatura"] == 0:
        print("Não há fatura a pagar.")
        return

    if conta["saldo_fatura"] > conta["saldo"]:
        print("Saldo insuficiente para pagar a fatura.")
        return

    valor_pago = conta["saldo_fatura"]
    conta["saldo"] -= valor_pago
    conta["saldo_fatura"] = 0.0
    registrar_historico(conta, "Pagamento de Fatura", valor_pago)
    print(f"Fatura de R$ {valor_pago:.2f} paga com sucesso.")


def menu_cartao():
    while True:
        print("\n--- Cartão de Crédito ---")
        print("[1] Comprar no crédito")
        print("[2] Pagar fatura")
        print("[3] Voltar")
        escolha = input("> ")

        if escolha == "1":
            comprar_no_credito()
        elif escolha == "2":
            pagar_fatura()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
