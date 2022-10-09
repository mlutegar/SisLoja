# PARTICIPAÇÃO
# Michel Lutegar D'Orsi Pereira TA
# Andre TA
# Gabriel TA #

def verifica_cpf(cpf):  # Função para verificar se o CPF é válido ou não
    # 1.º VERIFICAÇÃO (SOMA DOS DIGITOS TEM QUE TER DOIS ALGARISMOS IGUAIS)
    soma = 0
    cpf_test = int(cpf)

    for i in range(11):
        soma += cpf_test % 10
        cpf_test = cpf_test // 10

    if not (soma % 10 == soma // 10):
        return False

    # 2.º VERIFICAÇÃO (A UF DO DONO DE CPF TEM QUE SER IGUAL A UF DESCRITA NO CPF)
    uf = input("Digite UF: ")
    uf = uf.upper()  # Colocando UF escrita pelo usuario em maiusculo, para evitar problemas

    cpf_test = int(cpf)
    cpf_test = cpf_test // 100

    codigo_estado = cpf_test % 10

    if (codigo_estado == 0) and (uf == 'RS'):
        verificacao = True
    elif (codigo_estado == 1) and (uf == 'DF' or uf == 'GO' or uf == 'MT' or uf == 'MS' or uf == 'TO'):
        verificacao = True
    elif (codigo_estado == 2) and (uf == 'PA' or uf == 'AM' or uf == 'AC' or uf == 'AP' or uf == 'RO' or uf == 'RR'):
        verificacao = True
    elif (codigo_estado == 3) and (uf == 'CE' or uf == 'MA' or uf == 'PI'):
        verificacao = True
    elif (codigo_estado == 4) and (uf == 'PE' or uf == 'RN' or uf == 'PA' or uf == 'AL'):
        verificacao = True
    elif (codigo_estado == 5) and (uf == 'BA' or uf == 'SE'):
        verificacao = True
    elif (codigo_estado == 6) and (uf == 'MG'):
        verificacao = True
    elif (codigo_estado == 7) and (uf == 'RJ' or uf == 'ES'):
        verificacao = True
    elif (codigo_estado == 8) and (uf == 'SP'):
        verificacao = True
    elif (codigo_estado == 9) and (uf == 'PR' or uf == 'SC'):
        verificacao = True
    else:
        verificacao = False

    return verificacao


def menuprincipal(c_cpf, c_renda):  # Menu do Gerenciamento de Clientes

    # TITULO DO MENU
    print("\n" * 100)  # Limpando a tela
    print("-" * 30)
    print("Sistema de cadastro de cliente")
    print("-" * 30)

    # CADASTRO DE CPF COM RENDA
    while True:
        cpf = input("Digite o CPF do cliente que deseja adicionar (Se quiser parar, digite 0): ")
        if cpf != "0":
            if verifica_cpf(cpf):
                print("O CPF é valido.")
                print("-" * 30)
                c_cpf.append(cpf)
                c_renda.append(float(input("Digite a sua renda: ")))
                print("Operação realizada com sucesso!\n")
            else:
                print("CPF é invalido, tente novamente.\n")
                continue
        else:
            break

    # CALCULO DE PERCENTUAL DE CLIENTES
    qtd_total = len(c_cpf)
    qtd_classealta = 0
    qtd_classemedia = 0
    qtd_classebaixa = 0

    for i in range(qtd_total):
        if c_renda[i] >= 10000:
            qtd_classealta += 1
        elif c_renda[i] >= 5000:
            qtd_classemedia += 1
        elif c_renda[i] < 5000:
            qtd_classebaixa += 1

    # IMPRIMIR RESULTADO
    print("\n"*100)
    print('-' * 30)
    print('OPERAÇÃO REALIZADA COM SUCESSO')
    print('Total de clientes cadastrados:', qtd_total)
    print('-' * 60)
    if qtd_total != 0:
        print('FAIXA', '\t' * 9, 'PORCENTAGEM')
        print("Menor que R$ 5.000,00", '\t' * 5, (qtd_classebaixa / qtd_total) * 100, '%')
        print("Entre R$ 5.000,00 e R$ 10.000,00", '\t' * 2, (qtd_classemedia / qtd_total) * 100, '%')
        print("Maior R$ 10.000,00", '\t' * 6, (qtd_classealta / qtd_total) * 100, '%')
        print('-' * 60)
    a = int(input('Tecla 0 para retornar à tela principal: '))
    if a == 0:
        return "0"
