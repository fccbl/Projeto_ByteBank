from clientes import selecionar_conta, buscar_conta


def consultar_extrato():
    conta = selecionar_conta()
    if conta is None:
        return

    if not conta["historico"]:
        print("Não há transações no extrato.")
        return

    print(f"\nExtrato de {conta['nome']}:")
    for movimento in conta["historico"]:
        linha = f"{movimento['tipo']}: R$ {movimento['valor']:.2f}"
        if movimento["categoria"] is not None:
            linha += f" ({movimento['categoria']})"
        print(linha)


def estornar_ultima_transacao():
    conta = selecionar_conta()
    if conta is None:
        return

    if not conta["historico"]:
        print("Não há transações para estornar.")
        return

    ultima = conta["historico"].pop()
    tipo = ultima["tipo"]
    valor = ultima["valor"]
    detalhes = ultima["detalhes"]

    if tipo == "Depósito":
        conta["saldo"] -= valor
    elif tipo == "Saque":
        conta["saldo"] += valor
        conta["pontos"] -= detalhes["pontos_ganhos"]
    elif tipo == "Transferência":
        conta["saldo"] += valor
        conta["pontos"] -= detalhes["pontos_ganhos"]
        conta_destino = buscar_conta(ultima["destino"])
        if conta_destino is not None:
            conta_destino["saldo"] -= valor
    elif tipo == "Guardar no Cofrinho":
        conta["saldo"] += valor
        conta["cofrinhos"][detalhes["caixinha"]] -= valor
    elif tipo == "Resgatar do Cofrinho":
        conta["saldo"] -= valor
        conta["cofrinhos"][detalhes["caixinha"]] += valor
    elif tipo == "Rendimento de Cofrinho":
        conta["cofrinhos"][detalhes["caixinha"]] -= valor
    elif tipo == "Compra no Crédito":
        conta["saldo_fatura"] -= valor
    elif tipo == "Pagamento de Fatura":
        conta["saldo"] += valor
        conta["saldo_fatura"] += valor
    elif tipo == "Compra de Moeda":
        conta["saldo"] += valor
        conta["saldos_moedas"][detalhes["moeda"]] -= detalhes["quantidade"]
    elif tipo == "Venda de Moeda":
        conta["saldo"] -= valor
        conta["saldos_moedas"][detalhes["moeda"]] += detalhes["quantidade"]
    elif tipo == "Resgate de Cashback":
        conta["saldo"] -= valor
        conta["pontos"] += detalhes["pontos_usados"]
    elif tipo == "Empréstimo Contratado":
        conta["saldo"] -= valor
        conta["emprestimos"].remove(detalhes["emprestimo"])
    elif tipo == "Pagamento de Parcela":
        conta["saldo"] += valor
        detalhes["emprestimo"]["parcelas_pagas"] -= 1
    elif tipo == "Pagamento de Boleto":
        conta["saldo"] += valor
        conta["fila_pagamentos"].insert(0, {"nome": detalhes["nome_boleto"], "valor": valor})

    print(f"{tipo} de R$ {valor:.2f} estornado(a).")


def menu_extrato():
    while True:
        print("\n--- Extrato e Estorno ---")
        print("[1] Consultar extrato")
        print("[2] Estornar última transação")
        print("[3] Voltar")
        escolha = input("> ")

        if escolha == "1":
            consultar_extrato()
        elif escolha == "2":
            estornar_ultima_transacao()
        elif escolha == "3":
            break
        else:
            print("Opção inválida.")
