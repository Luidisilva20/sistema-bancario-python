import json
from datetime import datetime

# Função para inicializar a conta, carregando de um arquivo, se possível
def inicializar_conta(nome_arquivo="conta.json"):
    try:
        with open(nome_arquivo, "r") as f:
            dados_conta = json.load(f)
            return dados_conta
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existir ou estiver corrompido, cria uma conta nova
        return {
            "saldo": 0.0,
            "extrato": [],
        }

# Função para salvar a conta em um arquivo
def salvar_conta(conta, nome_arquivo="conta.json"):
    with open(nome_arquivo, "w") as f:
        json.dump(conta, f, indent=4)

# Função para realizar um depósito
def depositar(conta, valor):
    if valor <= 0:
        print("O valor do depósito deve ser positivo!")
        return
    conta["saldo"] += valor
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conta["extrato"].append(f"[{data}] Depósito: R${valor:.2f}")
    print(f"Depósito de R${valor:.2f} realizado com sucesso!")

# Função para realizar um saque
def sacar(conta, valor):
    if valor <= 0:
        print("O valor do saque deve ser positivo!")
        return
    if conta["saldo"] >= valor:
        conta["saldo"] -= valor
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conta["extrato"].append(f"[{data}] Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

# Função para transferir dinheiro entre contas
def transferir(conta_origem, conta_destino, valor):
    if valor <= 0:
        print("O valor da transferência deve ser positivo!")
        return
    if conta_origem["saldo"] >= valor:
        conta_origem["saldo"] -= valor
        conta_destino["saldo"] += valor
        
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conta_origem["extrato"].append(f"[{data}] Transferência para conta destino: R${valor:.2f}")
        conta_destino["extrato"].append(f"[{data}] Transferência recebida: R${valor:.2f}")
        
        print(f"Transferência de R${valor:.2f} realizada com sucesso!")
    else:
        print("Saldo insuficiente para transferência!")

# Função para exibir o extrato completo com data
def exibir_extrato(conta):
    print("\n--- Extrato ---")
    if not conta["extrato"]:
        print("Nenhuma transação realizada.")
    else:
        for transacao in conta["extrato"]:
            print(transacao)
    print(f"Saldo atual: R${conta['saldo']:.2f}")
    print("----------------")

# Função para exibir um relatório completo
def relatorio(conta):
    print("\n--- Relatório Completo ---")
    print(f"Saldo Total: R${conta['saldo']:.2f}")
    print(f"Total de Transações: {len(conta['extrato'])}")
    exibir_extrato(conta)

# Função para garantir que o valor inserido seja um número válido
def entrada_valida(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Por favor, insira um valor positivo.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")

# Função principal para interação com o usuário
def sistema_bancario():
    conta = inicializar_conta()

    while True:
        print("\n--- Sistema Bancário ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Extrato")
        print("4. Transferir")
        print("5. Relatório Completo")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = entrada_valida("Digite o valor do depósito: R$")
            depositar(conta, valor)
        elif opcao == "2":
            valor = entrada_valida("Digite o valor do saque: R$")
            sacar(conta, valor)
        elif opcao == "3":
            exibir_extrato(conta)
        elif opcao == "4":
            print("\nTransferir entre contas:")
            valor = entrada_valida("Digite o valor da transferência: R$")
            nome_destino = input("Digite o nome da conta destino: ")  
            print(f"Transferindo para a conta {nome_destino}...")
            transferir(conta, conta, valor)  
        elif opcao == "5":
            relatorio(conta)
        elif opcao == "6":
            salvar_conta(conta)
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executando o sistema bancário
if __name__ == "__main__":
    sistema_bancario()
