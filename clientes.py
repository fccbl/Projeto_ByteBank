contas = [
    {
        "nome": "Ana Clara Fornellos",
        "chave_pix": "ana@bytebank",
        "saldo": 500.0,
        "cofrinhos": {},
        "historico": [],
        "pontos": 0,
        "limite_credito": 1000.0,
        "saldo_fatura": 0.0,
        "saldos_moedas": {},
        "emprestimos": [],
    },
    {
        "nome": "Fabiana Lima",
        "chave_pix": "fabiana@bytebank",
        "saldo": 300.0,
        "cofrinhos": {},
        "historico": [],
        "pontos": 0,
        "limite_credito": 800.0,
        "saldo_fatura": 0.0,
        "saldos_moedas": {},
        "emprestimos": [],
    },
    {
        "nome": "Cliente Teste",
        "chave_pix": "teste@bytebank",
        "saldo": 1000.0,
        "cofrinhos": {},
        "historico": [],
        "pontos": 0,
        "limite_credito": 2000.0,
        "saldo_fatura": 0.0,
        "saldos_moedas": {},
        "emprestimos": [],
    },
]

clientes_removidos = []


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


def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    chave_pix = input("Chave PIX: ")
    if buscar_conta(chave_pix) is not None:
        print("Já existe uma conta com essa chave PIX.")
        return

    saldo_str = input("Saldo inicial (Enter para 0): ")
    if saldo_str.strip() == "":
        saldo_inicial = 0.0
    else:
        try:
            saldo_inicial = float(saldo_str)
        except ValueError:
            print("Valor inválido. Cadastro cancelado.")
            return
        if saldo_inicial < 0:
            print("O saldo inicial não pode ser negativo.")
            return

    contas.append(
        {
            "nome": nome,
            "chave_pix": chave_pix,
            "saldo": saldo_inicial,
            "cofrinhos": {},
            "historico": [],
            "pontos": 0,
            "limite_credito": 500.0,
            "saldo_fatura": 0.0,
            "saldos_moedas": {},
            "emprestimos": [],
        }
    )
    print(f"Cliente {nome} cadastrado com sucesso.")


def remover_cliente():
    conta = selecionar_conta()
    if conta is None:
        return

    confirmacao = input(f"Confirma remoção de {conta['nome']}? (s/n): ")
    if confirmacao.lower() != "s":
        print("Remoção cancelada.")
        return

    contas.remove(conta)
    clientes_removidos.append(conta)
    print(f"Cliente {conta['nome']} removido.")


def editar_cliente():
    conta = selecionar_conta()
    if conta is None:
        return

    novo_nome = input(f"Novo nome (Enter para manter '{conta['nome']}'): ")
    if novo_nome.strip():
        conta["nome"] = novo_nome

    nova_chave = input(f"Nova chave PIX (Enter para manter '{conta['chave_pix']}'): ")
    if nova_chave.strip():
        if buscar_conta(nova_chave) is not None:
            print("Já existe uma conta com essa chave PIX. Chave não alterada.")
        else:
            conta["chave_pix"] = nova_chave

    print("Dados atualizados com sucesso.")


def menu_clientes():
    while True:
        print("\n--- Gerenciar Clientes ---")
        print("[1] Cadastrar cliente")
        print("[2] Remover cliente")
        print("[3] Editar cliente")
        print("[4] Voltar")
        escolha = input("> ")

        if escolha == "1":
            cadastrar_cliente()
        elif escolha == "2":
            remover_cliente()
        elif escolha == "3":
            editar_cliente()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")
