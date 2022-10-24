# PARTICIPAÇÃO
# Michel Lutegar D'Orsi Pereira TA
# Andre TA
# Gabriel TA #


# MÓDULOS
import GerCaixa
import GerCliente
import GerEstoque
import os


# FUNÇÕES
def menu():
    print("\n" * 100)  # Limpar tela no PyCharm
    os.system('cls')  # Limpar tela no executavel
    print('-' * 30)
    print('SISTEMA DE GESTÃO DE LOJA (SisLoja)')
    print('Selecionar a opção desejada:')
    print('Gestão de estoque (1)')
    print('Gestão de clientes (2)')
    print('Gestão de fluxo de caixa (3)')
    print('-' * 30)
    return input('Insira(1,2,3): ')



# LISTAS
eCodigo, eDesc, eValor, eQtd = [], [], [], []  # Listas para gestão de estoque.
cCPF, cRenda = [], []  # Listas para gestão de clientes.
cVendaTotal = []  # Listas para gestão de caixa.

# SISTEMA DE ESCOLHAS
escolha = menu()
while True:
    if escolha == "1":
        escolha = GerEstoque.menuprincipal(eCodigo, eDesc, eValor, eQtd)
    elif escolha == "2":
        escolha = GerCliente.menuprincipal(cCPF, cRenda)
    elif escolha == "3":
        escolha = GerCaixa.menuprincipal(cCPF, eCodigo, eDesc, eValor, eQtd)

    escolha = menu()  # Se o usuario não digitar nenhum dos números, será executado o menu novamente.
