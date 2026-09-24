from clientes import buscar_conta, selecionar_conta

CATEGORIAS = ["Alimentação", "Transporte", "Lazer", "Contas", "Outros"]


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


def escolher_categoria():
    print("\nCategorias disponíveis:")
    for indice, categoria in enumerate(CATEGORIAS, start=1):
        print(f"[{indice}] {categoria}")

    escolha = input("Escolha a categoria: ")
    try:
        indice = int(escolha) - 1
        if 0 <= indice < len(CATEGORIAS):
            return CATEGORIAS[indice]
    except ValueError:
        pass

    print("Categoria inválida, marcando como 'Outros'.")
    return "Outros"


def registrar_historico(conta, tipo, valor, categoria=None, destino=None, detalhes=None):
    conta["historico"].append(
        {
            "tipo": tipo,
            "valor": valor,
            "categoria": categoria,
            "destino": destino,
            "detalhes": detalhes,
        }
    )


def adicionar_pontos(conta, valor):
    pontos_ganhos = int(valor // 10)
    conta["pontos"] += pontos_ganhos
    return pontos_ganhos


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
    registrar_historico(conta, "Depósito", valor)
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

    categoria = escolher_categoria()
    conta["saldo"] -= valor
    pontos_ganhos = adicionar_pontos(conta, valor)
    registrar_historico(conta, "Saque", valor, categoria, detalhes={"pontos_ganhos": pontos_ganhos})
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

    categoria = escolher_categoria()
    conta_origem["saldo"] -= valor
    conta_destino["saldo"] += valor
    pontos_ganhos = adicionar_pontos(conta_origem, valor)
    registrar_historico(
        conta_origem,
        "Transferência",
        valor,
        categoria,
        destino=conta_destino["chave_pix"],
        detalhes={"pontos_ganhos": pontos_ganhos},
    )
    print(
        f"Transferência de R$ {valor:.2f} de {conta_origem['nome']} "
        f"para {conta_destino['nome']} realizada com sucesso."
    )


def relatorio_categoria():
    conta = selecionar_conta()
    if conta is None:
        return

    totais = {}
    total_geral = 0.0
    for movimento in conta["historico"]:
        if movimento["categoria"] is None:
            continue
        totais[movimento["categoria"]] = totais.get(movimento["categoria"], 0.0) + movimento["valor"]
        total_geral += movimento["valor"]

    if not totais:
        print("Não há gastos registrados ainda.")
        return

    print(f"\nRelatório de gastos de {conta['nome']}:")
    for categoria, total in totais.items():
        percentual = (total / total_geral) * 100
        print(f"{categoria}: R$ {total:.2f} ({percentual:.1f}%)")
