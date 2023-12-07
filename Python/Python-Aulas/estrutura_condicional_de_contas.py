CONTA_1 = ("conta 1")
CONTA_2 = ("conta 2")
CONTA_3 = ("conta 3")

saldo_conta_1 = float(5000)
saldo_conta_2 = float(10000)
saldo_conta_3 = float(8000)


selecao_da_conta = input("Selecione a conta: ")
saque = float(input("Qual valor deseja retirar? "))

if selecao_da_conta >= CONTA_1:
    if saque <= saldo_conta_1:
        print("Saque realizado com sucesso ! ")
    else:
        print("Saldo insuficiente !")

if selecao_da_conta >= CONTA_2:
    if saque <= saldo_conta_2:
        print("Saque realizado com sucesso ! ")
    else:
        print("Saldo insuficiente !")

if selecao_da_conta >= CONTA_3:
    if saque <= saldo_conta_3:
        print("Saque realizado com sucesso ! ")
    else:
        print("Saldo insuficiente !")

