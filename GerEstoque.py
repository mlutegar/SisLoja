# PARTICIPAÇÃO
# Michel Lutegar D'Orsi Pereira TA
# Andre TA
# Gabriel TA #

def verifica_maior_20(n):  # Função para verificar se o código digitado é valido (a soma precisa ser superior a 20)
    n = str(n)  # Transformando número inteiro digitado para string
    soma_codigo = 0
    for i in range(len(n)):
        soma_codigo += int(n[i])

    if soma_codigo > 20:
        return True
    else:
        return False


def menuprincipal(e_codigo, e_desc, e_valor, e_qtd):
    # VARIAVEIS DA FUNÇÃO
    p = 1
    pos = 0
    codigo_maior_valor = ""
    maior_valor = 0
    soma_valor = 0

    # INTERFACE DO MENU
    print("\n" * 100)  # Limpando a tela
    print('GESTÃO DE ESTOQUE:')
    print(f'Deseja incluir item(s): Digite (1)')
    print(f'Deseja excluir item(s): Digite (2)')
    print('-' * 30)
    escolha = int(input('Insira(1 ou 2): '))

    # CÓDIGO PARA ADICIONO DE ITENS
    if escolha == 1:
        # INPUT DA QUANTIDADE DE ITENS QUE SERÃO CADASTRADOS
        n = int(input("Quantos itens deseja inserir? "))

        # INPUT DE VALORES REFERENTE AO ITEM
        for i in range(n):
            # INPUT DO CÓDIGO DO ITEM
            while True:
                cod_item = int(input('\nCódigo do produto: '))

                if verifica_maior_20(cod_item):
                    e_codigo.append(int(cod_item))
                    break
                else:
                    print("Código invalido! A soma dos códigos precisa ser maior do que 20. Preencha novamente!")
                    continue

            # INPUT DA DESCRIÇÃO, VALOR E QUANTIDADE DO ITEM
            desc_item = input('Descrição do produto: ')
            e_desc.append(desc_item)

            valor_item = float(input('Valor do produto: R$ '))
            soma_valor += valor_item
            e_valor.append(valor_item)

            qtd_item = int(input('Quantidade do produto: '))
            e_qtd.append(qtd_item)

            # VERIFICAÇÃO DO PRODUTO COM MAIOR VALOR
            if valor_item > maior_valor:
                maior_valor = valor_item
                codigo_maior_valor = cod_item

        # CALCULO DA MÉDIA DOS PRODUTOS CADASTRADOS AGORA
        media = soma_valor / n

        if n != 0:
            print('-' * 30)
            print(f"Média dos itens cadastrados: R$ {media}")
            print(f"Item de maior valor cadastrado: código {codigo_maior_valor}, valor R$ {maior_valor}")
        else:
            print("Nenhum item incluido.")

        print('-' * 30)
        e = int(input("Teclar 0 para retornar à tela pricipal "))
        if e == 0:
            print("\n" * 100)  # Limpando a tela
            return "0"

    # CÓDIGO PARA EXCLUSÃO DE ITENS
    elif escolha == 2:

        # VERIFICAÇÃO SE HÁ PRODUTO PARA EXCLUIR
        if len(e_codigo) == 0:
            print("Não há nenhum produto no estoque para remover. Retornando para o menu")
            return "1"

        # PROCESSO DE EXCLUSÃO
        item_exclusao = []  # Lista para guardar as posições dos itens que serão mostrados no relatorio de exclusão
        while p != 0:
            # INPUT DO CÓDIGO DO ITEM
            item_desejado = input("\nQual o código do item que deseja excluir? ")

            # VERIFICAÇÃO DE VALIDEZ DO CÓDIGO
            codigo_cadastrado = False  # Variavel que verifica se o código está ou não cadastrado

            if not verifica_maior_20(item_desejado):
                print("Código possui estrutura invalida!")
                continue

            for i in range(len(e_codigo)):
                if e_codigo[i] == int(item_desejado):
                    codigo_cadastrado = True

            if not codigo_cadastrado:
                print("Código não cadastrado. Insira um código válido.")
                continue

            # EXCLUSÃO DO ITEM
            certeza = int(input("Tem certeza? (1 pra sim, 2 pra nao) "))

            if certeza == 1:
                # PEGAR A POSIÇÃO DO ITEM NA LISTA PARA FAZE A EXCLUSÃO
                for i in range(len(e_codigo)):
                    if int(item_desejado) == e_codigo[i]:
                        pos = i
                        item_exclusao.append(pos)
                        break

                # INPUT DA QUANTIDADES DO ITEM QUE VAI SER REMOVIDO
                print('\nItens disponíveis', e_qtd[pos])

                while True:
                    remov = int(input("Quantos unidades você quer remover?"))
                    if remov > e_qtd[pos]:
                        print(f"A quantidade desejada ultrapassa a quantidade que há no estoque!\n")
                        continue
                    else:
                        break

                e_qtd[pos] -= remov

                # RESULTADO PARCIAL DA EXCLUSÃO
                print("\nOperação realizada com sucesso")
                print("O produto de código", item_desejado, "tem agora:", e_qtd[pos], "itens")

                # VOLTA PARA O MENU
                p = int(input("\nQuer continuar? (1 para sim, 0 para não): "))
            elif certeza == 2:
                continue

        # RESULTADO FINAL DA EXCLUSÃO
        print("-" * 30)
        print("RELATÓRIO DE ITENS EXCLUÍDOS")
        print("ITEM \t\t SALDO")
        item_exclusao = list(set(item_exclusao))  # Tirando os valores repetidos da lista
        for i in range(len(item_exclusao)):
            print(e_codigo[item_exclusao[i]], '\t\t', e_qtd[item_exclusao[i]])
        print("-" * 30, "\n")

        # CÓDIGO PARA RETORNAR PARA A PÁGINA PRINCIPAL
        e = int(input("Teclar 0 para retornar à tela pricipal "))
        if e == 0:
            print("\n" * 100)  # Limpando a tela
            return "0"
