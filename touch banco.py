saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
============ BANCO DIO ============

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

while True:
    opcao = input(menu)

    # DEPÓSITO
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. Informe um valor positivo.")

    # SAQUE
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: R$ "))

        if valor > saldo:
            print("❌ Saldo insuficiente.")
        elif valor > limite:
            print("❌ Valor acima do limite por saque (R$500).")
        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Limite diário de saques atingido (3 saques).")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido. Informe um valor positivo.")

    # EXTRATO
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================")

    # SAIR
    elif opcao == "0":
        print("Obrigado por usar o Banco LCS. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")


