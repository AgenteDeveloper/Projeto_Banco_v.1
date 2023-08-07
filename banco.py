menu = """

Seja bem vindo ao seu sistema bancário!

Selecione uma das operações abaixo para continuar:

[D] - Depositar
[S] - Sacar
[E] - Extrato
[Q] - Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_diario = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Insira o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"
            print("Valor depositado com sucesso!")
        else:
            print("Valor inserido inválido, tente novamente") 


    elif opcao == "S":
        valor = float(input("Insira o valor a ser sacado: "))

        execede_saldo = valor > saldo

        execede_limite = valor > limite

        execede_diario = numero_saques >= limite_diario

        if execede_saldo:
            print("Valor inserido é maior do que seu saldo. Tente novamente")
        
        elif execede_limite:
            print("Valor maior que limite permitido. Tente novamente")
        
        elif execede_diario:
            print("Limite diário alcançado, tente novamente amanhã.")

        elif valor > 0:
            saldo -= valor

            extrato += f"Saque: R$ {valor:.2f} \n"

            numero_saques += 1

            print("Valor sacado com sucesso")
        else:
           print("Valor inserido inválido, tente novamente") 

    elif opcao == "E":
        print("\n<<<<<<Extrato>>>>>")
        print("Sem movimentações na conta" if not extrato else extrato)
        print( f"\nSaque: R$ {valor:.2f}")
        print("<<<<<<<<<>>>>>>>>>")



    elif opcao == "Q":
        break    

    else:
        print("Operação inexistente, tente novamente com uma das opções disponiveis")        
