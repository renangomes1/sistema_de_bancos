# Crie um sistema de banco, com as seguintes operações:

# # SISTEMA DE BANCO 

# - Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 

















Nome = input('Digite seu nome>>')
CPF = input('Digite seu CPF>>')
Senha = input('Digite sua senha>>')
print(f'Olá {Nome}, Seja bem vindo(a)!')

print('Escolha uma das opções abaixo:')
print('OBS: Escolha um número para uma da opções desejadas')




saldo = 0

def menu():
    print('BANCO')
    print('1. Ver extrato')
    print("2. Fazer um depósito")
    print("3. Fazer um saque")
    print("4. Sair do sistema")

def ver_extrato():
    print(f"Saldo atual: R${saldo:.2f}")

def fazer_deposito():
    global saldo
    valor = int(input("Digite o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

def fazer_saque():
    global saldo
    valor = float(input("Digite o valor do saque: R$"))
    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    

def main():
    while True:
        menu()
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            ver_extrato()
        elif opcao == '2':
            fazer_deposito()
        elif opcao == '3':
            fazer_saque()
        elif opcao == '4':
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida, por favor escolha uma opção válida.')


main()