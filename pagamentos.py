from clientes import selecionar_conta
from operacoes import ler_valor, registrar_historico


def agendar_pagamento():
    conta = selecionar_conta()
    if conta is None:
        return

    nome_boleto = input("Nome do boleto/pagamento: ")
    valor = ler_valor("Valor do boleto: ")
    if valor is None:
        return

    conta["fila_pagamentos"].append({"nome": nome_boleto, "valor": valor})
    print(f"Boleto '{nome_boleto}' de R$ {valor:.2f} agendado.")


def consultar_fila_pagamentos():
    conta = selecionar_conta()
    if conta is None:
        return

    if not conta["fila_pagamentos"]:
        print("Não há boletos agendados.")
        return

    print(f"\nBoletos agendados de {conta['nome']} (ordem de chegada):")
    for boleto in conta["fila_pagamentos"]:
        print(f"{boleto['nome']}: R$ {boleto['valor']:.2f}")


def processar_pagamentos():
    conta = selecionar_conta()
    if conta is None:
        return

    if not conta["fila_pagamentos"]:
        print("Não há boletos agendados.")
        return

    print(f"\nProcessando pagamentos de {conta['nome']} na ordem de chegada:")
    while conta["fila_pagamentos"]:
        boleto = conta["fila_pagamentos"][0]
        if boleto["valor"] > conta["saldo"]:
            print(f"Saldo insuficiente para pagar '{boleto['nome']}'. Processamento interrompido.")
            return

        conta["fila_pagamentos"].pop(0)
        conta["saldo"] -= boleto["valor"]
        registrar_historico(conta, "Pagamento de Boleto", boleto["valor"], detalhes={"nome_boleto": boleto["nome"]})
        print(f"'{boleto['nome']}' pago: R$ {boleto['valor']:.2f}")

    print("Todos os boletos foram processados.")


def menu_pagamentos():
    while True:
        print("\n--- Fila de Pagamentos Agendados ---")
        print("[1] Agendar pagamento")
        print("[2] Consultar fila")
        print("[3] Processar pagamentos (virada de lote)")
        print("[4] Voltar")
        escolha = input("> ")

        if escolha == "1":
            agendar_pagamento()
        elif escolha == "2":
            consultar_fila_pagamentos()
        elif escolha == "3":
            processar_pagamentos()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
