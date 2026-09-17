from clientes import selecionar_conta
from operacoes import ler_valor

TAXAS_CAMBIO = {"USD": 5.50, "EUR": 6.00, "BTC": 350000.0}


def comprar_moeda_estrangeira():
    conta = selecionar_conta()
    if conta is None:
        return

    moeda = input(f"Moeda ({'/'.join(TAXAS_CAMBIO)}): ").upper()
    if moeda not in TAXAS_CAMBIO:
        print("Moeda não suportada.")
        return

    valor_brl = ler_valor("Valor em reais a converter: ")
    if valor_brl is None:
        return

    if valor_brl > conta["saldo"]:
        print("Saldo insuficiente.")
        return

    quantidade = valor_brl / TAXAS_CAMBIO[moeda]
    conta["saldo"] -= valor_brl
    conta["saldos_moedas"][moeda] = conta["saldos_moedas"].get(moeda, 0.0) + quantidade
    print(f"Compra de {quantidade:.6f} {moeda} realizada.")


def vender_moeda_estrangeira():
    conta = selecionar_conta()
    if conta is None:
        return

    moeda = input(f"Moeda ({'/'.join(TAXAS_CAMBIO)}): ").upper()
    if moeda not in TAXAS_CAMBIO:
        print("Moeda não suportada.")
        return

    saldo_moeda = conta["saldos_moedas"].get(moeda, 0.0)
    quantidade_str = input(f"Quantidade de {moeda} a vender: ")
    try:
        quantidade = float(quantidade_str)
    except ValueError:
        print("Valor inválido.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    if quantidade > saldo_moeda:
        print("Saldo insuficiente dessa moeda.")
        return

    valor_brl = quantidade * TAXAS_CAMBIO[moeda]
    conta["saldos_moedas"][moeda] -= quantidade
    conta["saldo"] += valor_brl
    print(f"Venda de {quantidade:.6f} {moeda} convertida em R$ {valor_brl:.2f}.")


def menu_cambio():
    while True:
        print("\n--- Câmbio de Moedas ---")
        print("[1] Comprar moeda estrangeira")
        print("[2] Vender moeda estrangeira")
        print("[3] Voltar")
        escolha = input("> ")

        if escolha == "1":
            comprar_moeda_estrangeira()
        elif escolha == "2":
            vender_moeda_estrangeira()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
