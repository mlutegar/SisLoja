# PARTICIPAÇÃO
# Michel Lutegar D'Orsi Pereira TA
# Andre TA
# Gabriel TA #

def menuprincipal(c_cpf, e_codigo, e_desc, e_valor, e_qtd):
    # INTERFACE DO MENU
    print("\n" * 100)  # Limpando a tela
    print("-" * 30)
    print("Gerenciamento de Caixa")
    print("-" * 30)

    # VERIFICAÇÃO SE HÁ PRODUTO E CLIENTE PARA INICIAR O GER CAIXA
    if len(e_codigo) == 0 or len(c_cpf) == 0:
        print("Não há produto no estoque ou clientes cadastrado para começar uma venda no caixa.")
        a = int(input('Tecla 0 para retornar à tela principal: '))
        if a == 0:
            return "0"

    # VARIAVEIS
    tot_venda_cliente = 0
    tot_venda_final = 0
    maior_tot_venda = 0

    # INPUT DATA
    print("Digite o dia, o mês e o ano do inicio do lançamento de dados")
    dia = input("Dia: ")
    mes = input("Mês: ")
    ano = input("Ano: ")
    data = f"{dia}/{mes}/{ano}"

    # INPUT SALDO
    print('')
    saldo_inicial = float(input("Saldo inicial: "))
    n = int(input("Número de vendas: "))

    # INPUT DO CPF E VENDAS POR CLIENTE
    cpf_maior_consumo = ""
    print("-" * 30)
    for i in range(n):
        print("\nVenda número", i+1)

        # VERIFICA SE O CPF ESTÁ CADASTRADO
        cpf_cadastrado = False
        while not cpf_cadastrado:
            cpf = input("CPF do cliente: ")
            for o in range(len(c_cpf)):
                if c_cpf[o] == cpf:
                    cpf_cadastrado = True
            if not cpf_cadastrado:
                print("CPF não cadastrado. Insira um CPF válido.")

        # INPUT DA QUANTIDADE DE COMPRAS DO CLIENTE
        qtd_compras_cpf = int(input("Qtd compras do cliente: "))

        if cpf_cadastrado:
            # INPUT DOS DADOS DO PROTUDO QUE O CLIENTE COMPROU
            for e in range(qtd_compras_cpf):
                print("\nProduto", e+1)

                # VERIFICAR SE O PRODUTO ESTÁ CADASTRADO
                cod_cadastro = False
                while not cod_cadastro:
                    cod_item = int(input("Código do item: "))
                    for o in range(len(e_codigo)):
                        if e_codigo[o] == cod_item:
                            cod_cadastro = True
                    if not cod_cadastro:
                        print("Código não cadastrado. Insira um código válido.")

                # RESGATANDO O VALOR E DESCRIÇÃO DO PRODUTO
                valor_item = e_valor[e_codigo.index(cod_item)]
                desc_item = e_desc[e_codigo.index(cod_item)]
                qtd_item = e_qtd[e_codigo.index(cod_item)]
                print("Foi selecionado o produto", desc_item,
                      "que custa R$", valor_item,
                      "e há", qtd_item, "unidades")

                # INPUT E VERIFICAÇÃO DA QUANTIDADE UNITARIA DO PRODUTO QUE FOI COMPRADO
                while True:
                    qtd_comprado = int(input(f"Quantidade de {desc_item} comprados: "))
                    if qtd_comprado > qtd_item:
                        print(f"A quantidade desejada ultrapassa a quantidade de {desc_item} que há no estoque!\n")
                        continue
                    else:
                        break

                # ATUALIZANDO VALORES DAS VARIAVEIS
                e_qtd[e_codigo.index(cod_item)] -= qtd_comprado
                tot_venda_cliente += qtd_comprado * valor_item
                if tot_venda_cliente > maior_tot_venda:
                    maior_tot_venda = tot_venda_cliente
                    cpf_maior_consumo = cpf

        # RESULTADO PARCIAL
        print("-" * 40)
        print("Cliente", cpf, "Total de vendas: R$", tot_venda_cliente)
        tot_venda_final += tot_venda_cliente
        tot_venda_cliente = 0

    # RESULTADO FINAL
    print("-" * 40)
    print("Data da movimentação:", data)
    print("Saldo: R$", saldo_inicial+tot_venda_final)
    print("Valor médio das vendas: R$", tot_venda_final / n)
    print("Total vendas:", n, "unidades")
    print("Cliente de maior consumo: CPF", cpf_maior_consumo)
    print("-" * 40)
    a = input('Tecla 0 para retornar à tela principal: ')
    if a == '0':
        return '0'
