# ByteBank

Projeto da disciplina  Algoritmo e Estrutura de Dados, sistema bancário feito em Python.

## Integrantes

- Anna Clara Fornellos
- Fabiana Lima

## O que o sistema faz

O ByteBank é dividido em três níveis, como o projeto pediu:

- **Nível 1**: consultar saldo, depositar e sacar.
- **Nível 2**: várias contas guardadas na memória (com nome, chave PIX e saldo), transferência via PIX entre elas, e cadastro/edição/remoção de clientes (sem limite de quantidade).
- **Nível 3**: extrato com todas as movimentações e a opção de estornar a última transação (funciona como uma pilha), e uma fila de pagamentos agendados, processados na ordem em que foram cadastrados.

Também tem algumas funcionalidades extras, combinadas direto com o professor: cofrinhos de investimento, cartão de crédito, câmbio de moedas, pontos de fidelidade com cashback e empréstimos.

O programa roda em um menu que fica repetindo até o usuário escolher sair. Toda operação pede a chave PIX da conta pra saber onde mexer, e o sistema não deixa fazer depósito, saque ou transferência com valor inválido, negativo ou maior que o saldo disponível.

## Como o código está organizado

Cada arquivo cuida de uma parte do sistema:

- `main.py`: o menu principal, é o que você executa
- `clientes.py`: cadastro e dados das contas
- `operacoes.py`: saldo, depósito, saque, PIX e categorias de gasto
- `extrato.py`: extrato e estorno da última transação
- `pagamentos.py`: fila de pagamentos agendados
- `cofrinhos.py`, `cartao.py`, `cambio.py`, `fidelidade.py`, `emprestimos.py`: as funcionalidades extras

## Como executar

Com o Python instalado, basta rodar:

```
python main.py
```


