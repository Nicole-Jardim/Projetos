import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo usuário
    [6]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0 and valor < 500:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def fextrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================\n")


def adicionar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("Este cliente já está cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")


def filtrar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return None


def criar_conta(contas, agencia, cpf, clientes):
    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        numero_conta = len(contas) + 1
        conta = {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
        contas.append(conta)
        print("=== Conta criada com sucesso! ===")
    else:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")


def main():
    limite_saques = 3
    agencia = "0001"

    extrato = ""
    saldo = 0
    numero_saques = 0
    clientes = []
    contas = []
    limite = 500

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Qual o valor que deseja depositar? "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Qual o valor que deseja sacar? "))
            saldo, extrato, numero_saques = saque(saldo, valor, extrato, limite, numero_saques, limite_saques)

        elif opcao == "3":
            fextrato(saldo, extrato)

        elif opcao == "4":
            cpf = input("Informe o CPF do usuário: ")
            criar_conta(contas, agencia, cpf, clientes)

        elif opcao == "5":
            adicionar_cliente(clientes)

        elif opcao == "6":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
