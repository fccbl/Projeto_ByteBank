import csv

from clientes import contas

ARQUIVO_CONTAS = "contas.csv"
CAMPOS = ["nome", "chave_pix", "saldo", "limite_credito", "saldo_fatura", "pontos"]


def salvar_contas_txt(contas):
    with open(ARQUIVO_CONTAS, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(CAMPOS)
        for conta in contas:
            escritor.writerow(
                [
                    conta["nome"].strip(),
                    conta["chave_pix"].strip(),
                    conta["saldo"],
                    conta["limite_credito"],
                    conta["saldo_fatura"],
                    conta["pontos"],
                ]
            )
    print(f"{len(contas)} conta(s) salva(s) em {ARQUIVO_CONTAS}.")


def limpar_linha(linha):
    nome = (linha["nome"] or "").strip()
    chave_pix = (linha["chave_pix"] or "").strip()
    if nome == "" or chave_pix == "":
        return None

    try:
        saldo = float(linha["saldo"])
        limite_credito = float(linha["limite_credito"])
        saldo_fatura = float(linha["saldo_fatura"])
        pontos = int(linha["pontos"])
    except (ValueError, TypeError):
        return None

    if saldo < 0 or limite_credito < 0 or saldo_fatura < 0 or pontos < 0:
        return None

    return {
        "nome": nome,
        "chave_pix": chave_pix,
        "saldo": saldo,
        "cofrinhos": {},
        "historico": [],
        "fila_pagamentos": [],
        "pontos": pontos,
        "limite_credito": limite_credito,
        "saldo_fatura": saldo_fatura,
        "saldos_moedas": {},
        "emprestimos": [],
    }


def carregar_contas_txt():
    contas_lidas = []
    chaves_vistas = []

    try:
        # "r" = modo de leitura.
        with open(ARQUIVO_CONTAS, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                conta = limpar_linha(linha)
                if conta is None:
                    print("Linha inválida ignorada no arquivo de contas.")
                elif conta["chave_pix"] in chaves_vistas:
                    print(f"Chave PIX repetida ignorada: {conta['chave_pix']}")
                else:
                    contas_lidas.append(conta)
                    chaves_vistas.append(conta["chave_pix"])
    except FileNotFoundError:
        print("Nenhum arquivo salvo encontrado. Iniciando com as contas padrão.")
        return
    
    contas.clear()
    contas.extend(contas_lidas)
    print(f"{len(contas)} conta(s) carregada(s) de {ARQUIVO_CONTAS}.")
