itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,        6.50,        7.00,    8.00   ]


clientes = []
faturamento = 0
todos_pedidos = []


while True:
    print()
    print("---------- CARDÁPIO ----------\n")
    for i, item in enumerate(itens):
        print(f"{i+1}. {item} ........ R$ {precos[i]:.2f}")
        
    nome_cliente = input("\nDigite seu nome (ou digite 'fim' para encerrar): ")
    
    if nome_cliente == "fim":
        break
    
    clientes.append(nome_cliente)

    pedidos_itens = []
    pedidos_precos = []

    while True:
        
        pedido_cliente = int(input("Digite o número do item desejado (ou digite '0' para finalizar): "))
        
        if pedido_cliente == 0:
            break
        
        pedidos_itens.append(itens[pedido_cliente-1])
        pedidos_precos.append(precos[pedido_cliente-1])
        
    print(f" ----- Pedido de {nome_cliente} -----")
    for i, item in enumerate(pedidos_itens):
        print(f"{i+1}. {item} ........ R$ {pedidos_precos[i]:.2f}")

    remover = input("\nDeseja remover algum item? (S/N)").lower()

    if remover == "s":
        num = (int(input("Digite o número do item: ")))
        num_remover = num - 1
        pedidos_itens.pop(num_remover)
        pedidos_precos.pop(num_remover)
        print("Pedido atualizado: ")
        for i, item in enumerate(pedidos_itens):
            print(f"{i+1}. {item} ........ R$ {pedidos_precos[i]:.2f}")

    elif remover == "":
        continue

    soma = sum(pedidos_precos)
    todos_pedidos.extend(pedidos_itens)

    if len(pedidos_itens) >= 4:
        desconto = soma *0.10
        total_final = soma - desconto
        print(f"Total inicial: R$ {soma:.2f}")
        print(f"Desconto aplicado (10%): R$ {desconto:.2f}")
        print(f"TOTAL FINAL (com desconto): R$ {total_final:.2f}")
        faturamento += total_final
   
    else:
        print(f"TOTAL: R$ {soma:.2f}")
        faturamento += soma

mais_pedido = ""
maior_qtd = 0

for item in itens:
    quantidade = todos_pedidos.count(item)
    if quantidade > maior_qtd:
        maior_qtd = quantidade
        mais_pedido = item

print(f"""
------ RELATÓRIO FINAL ------
      
    Total de clientes: {len(clientes)}
    Nome de todos os clientes: {clientes}
    Item mais caro: {max(pedidos_precos):.2f}
    Item mais barato: {min(pedidos_precos):.2f}
    Item mais pedido: {mais_pedido} ({maior_qtd} pedidos)
    Faturamento total: {faturamento:.2f}
""")