from clientes import selecionar_conta
from operacoes import registrar_historico


def consultar_pontos():
    conta = selecionar_conta()
    if conta is None:
        return

    print(f"\n{conta['nome']} tem {conta['pontos']} BytePoints.")


def resgatar_cashback():
    conta = selecionar_conta()
    if conta is None:
        return

    pontos_str = input("Quantos pontos deseja resgatar? ")
    try:
        pontos = int(pontos_str)
    except ValueError:
        print("Valor inválido.")
        return

    if pontos <= 0 or pontos > conta["pontos"]:
        print("Quantidade de pontos inválida.")
        return

    cashback = (pontos / 100) * 5
    conta["pontos"] -= pontos
    conta["saldo"] += cashback
    registrar_historico(conta, "Resgate de Cashback", cashback, detalhes={"pontos_usados": pontos})
    print(f"Resgate de {pontos} pontos convertido em R$ {cashback:.2f} de cashback.")


def menu_fidelidade():
    while True:
        print("\n--- Pontos e Cashback ---")
        print("[1] Consultar pontos")
        print("[2] Resgatar cashback")
        print("[3] Voltar")
        escolha = input("> ")

        if escolha == "1":
            consultar_pontos()
        elif escolha == "2":
            resgatar_cashback()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
