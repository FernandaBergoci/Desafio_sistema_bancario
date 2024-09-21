import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def sacar(valor, saldo_em_conta,extrato, qtdeSaque):
    
    if(valor<0):
        print("\nValor inválido")
    elif(saldo_em_conta<=0):
        print("\nSaldo insuficiente!")
    elif(valor<=saldo_em_conta):
        if(valor<=500):
            if(qtdeSaque<3):
                saldo_em_conta-=valor
                extrato.append(valor*-1.0)
                qtdeSaque+= 1
                print("\nSaque realizado com sucesso!!")
            else:
                print("\nERRO!! Máximo de 3 saques diários")
        else:
            print("\nValor máximo para saque excedido!") 
    else:
        print("\nSaldo Insuficiente!! Digite um valor menor")
    
    return saldo_em_conta, extrato, qtdeSaque

def depositar(valor, saldo_em_conta, extrato):
    if(valor>0):
        saldo_em_conta+=valor
        extrato.append(valor)
        print("\nDepósito realizado com sucesso!!")
    else:
        print("\nValor inválido")
    return saldo_em_conta, extrato

def mostrar_extrato(extrato, saldo_em_conta):
    print("\n================ EXTRATO ================")
    if(len(extrato) == 0):
        print("\nVocê não tem nenhum lançamento")
    else:
        for valor in extrato:
            if(valor>0):
                print(f"Depósito \tR$ {valor}")
            else:
                print(f"Saque \t\tR$ {valor}")
    print(f"\nSALDO \t\tR$ {saldo_em_conta}")
    print("=========================================")

def main():
    extrato =[]
    saldo_em_conta=0.0
    qtdeSaque=0
    resp='n'

    while(resp!='q'):
        resp = menu()
        if(resp == 'd'):
            valor = float(input("Digite o valor do depósito: "))
            saldo_em_conta, extrato = depositar(valor, saldo_em_conta,extrato)
        elif(resp=='s'):
            valor = float(input("Digite o valor do saque: "))
            saldo_em_conta, extrato, qtdeSaque = sacar(valor, saldo_em_conta,extrato, qtdeSaque)
        elif(resp=='e'):
            mostrar_extrato(extrato, saldo_em_conta)
        elif(resp=='q'):
            print("Operação finalizada")
        else:
            print("Opção inválida")

main()   