#Sistema Bancário

valortotal = 0
def saque(valortotal):
    valor = float(input("Digite o valor a ser sacado: "))
    if valor <= 500 and valor <= valortotal:
        valortotal = valortotal - valor
        print("Deposito efetuado com sucesso!")
    else: 
        print("Limite ultrapassado ou saldo insuficiente")
    return valortotal

def deposito(valortotal):
    valor = float(input("Digite o valor a ser depositado"))
    valortotal = valortotal + valor
    print(f"{valor} depositado em sua conta!")
    return valortotal

def extrato(valortotal):
    print(f"O saldo da sua conta é {valortotal}")
    return valortotal

def menu():
    print("Escolha uma opcao")
    print("Para saque digite 1")
    print("Para depósito digite 2")
    print("Para extrato digite 3")
    print("Para sair digite 4")
    return int(input("Escolha uma opcao"))
def main():
    valortotal = 0 
    opc = 0 
    while opc != 4:
        opc = menu()
        if opc == 1:
            valortotal = saque(valortotal)
        elif opc == 2:
            valortotal = deposito(valortotal)
        elif opc == 3: 
            valortotal = extrato(valortotal)
        elif opc == 4:
            print("Obrigada pela preferencia")
        else: 
            print("Opcao inválida")
        

main()