menu = """"
    BEM VINDO AO SISTEMA BANCÁRIO PYTHON
    -----------------------------------
     SELECIONE UMA DAS OPÇÕES ABAIXO:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    -----------------------------------

--> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Digite o valor de depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito deve ser positivo.")

    elif opcao == "2":
        valor_saque = float(input("Digite o valor de saque: "))
        if valor_saque > limite:
            print("Saque acima do limite permitido de R$ 500.00!")
        elif valor_saque < 0:
            print("Saque não pode ser negativo!")
        elif valor_saque > saldo: 
            print("Saque não realizado. Saldo insuficiente!")   
        elif numero_saques >= limite_saque:
            print ("Número de saques excedito!")
        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação não realizada. Tente novamente!")

    elif opcao == "3":
        print("Extrato solicitado:")
        print(extrato if extrato else "Nenhuma movimentação encontrada.")
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços!")
        break
    
    else:
        print("Opção inválida, digite a opção desejada.")
