#funçoes definidas pelo usuário

def calcular_desconto(valor, percentual):
    """calcula valor final aplicando um desconto percentual"""
    if percentual < 0 or percentual > 100:
        return None  # marcação inválida

    desconto = valor * (percentual / 100)
    return valor - desconto


def registrar_produto(produto, valor_final):
    """Imprime o registro de uma venda."""
    print(f"\nVenda registrada: {produto} por R$ {valor_final:.2f}")


#função lambda para arredondar
arredondar = lambda v: round(v, 2)


total_vendas = 0
qtd_vendas = 0

#Loop principal do caixa
while True:
    print("\n ---LOJA CASCA--- ")
    print(" 1- Registrar venda ")
    print(" 2- Ver relatório do dia ")
    print(" 3- Encerrar caixa ")

    opção = input("Escolha uma opção: ")

    if opção == "3":
        print("Encerrando o caixa. Até a próxima.")
       

    elif opção == "1":
        produto = input("Nome do produto: ")
        valor = float(input("Valor do produto:  R$"))
        percentual = float(input("Desconto (%):  "))

        valor_final = calcular_desconto(valor, percentual)

        if valor_final is None:
            print("Desconto inválido")
        else:
            valor_final = arredondar(valor_final)
            registrar_produto(produto, valor_final)
            total_vendas = total_vendas + valor_final
            qtd_vendas = qtd_vendas + 1

    elif opção == "2":
        print("\n --- Relatório de Vendas Diário --- ")
        print(f"Vendas de hoje: {qtd_vendas}")
        print(f"Total faturado: R$ {arredondar(total_vendas):.2f}")

    else:
        print("Opção inválida. Tente novamente.")
