from clientes import menu_clientes
from operacoes import consultar_saldo, depositar, sacar, transferir, relatorio_categoria
from cofrinhos import menu_cofrinhos
from cartao import menu_cartao
from cambio import menu_cambio
from fidelidade import menu_fidelidade
from emprestimos import menu_emprestimos


def exibir_menu():
    print("\n=== ByteBank ===\n")
    print("[1] Consultar Saldo")
    print("[2] Depositar")
    print("[3] Sacar")
    print("[4] Transferir (PIX)")
    print("[5] Gerenciar Clientes")
    print("[6] Cofrinhos de Investimento")
    print("[7] Relatório de Gastos por Categoria")
    print("[8] Cartão de Crédito")
    print("[9] Câmbio de Moedas")
    print("[10] Pontos e Cashback")
    print("[11] Empréstimos")
    print("[12] Sair")


def main():
    while True:
        exibir_menu()
        opcao = input("\n> Digite a operação desejada: ")

        if opcao == "1":
            consultar_saldo()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            transferir()
        elif opcao == "5":
            menu_clientes()
        elif opcao == "6":
            menu_cofrinhos()
        elif opcao == "7":
            relatorio_categoria()
        elif opcao == "8":
            menu_cartao()
        elif opcao == "9":
            menu_cambio()
        elif opcao == "10":
            menu_fidelidade()
        elif opcao == "11":
            menu_emprestimos()
        elif opcao == "12":
            print("\nObrigado por usar o ByteBank. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
