# ByteBank

Projeto da disciplina  Algoritmo e Estrutura de Dados, sistema bancário feito em Python.

## Integrantes

- Anna Clara Fornellos
- Fabiana Lima

## O que o sistema faz

- Consultar saldo
- Depositar
- Sacar
- Transferir via PIX entre contas

O programa roda em um menu que fica repetindo até o usuário escolher sair. As contas ficam guardadas em memória, cada uma com nome, chave PIX e saldo, e toda operação pede a chave PIX pra saber em qual conta mexer.

Ele não deixa fazer depósito ou saque com valor negativo ou zero, não deixa sacar ou transferir mais do que o saldo disponível, e a transferência só acontece se as chaves PIX de origem e destino existirem.

Mais pra frente o projeto vai ganhar extrato com estorno e fila de pagamentos agendados.


