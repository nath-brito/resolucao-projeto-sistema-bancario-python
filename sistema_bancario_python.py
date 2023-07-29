#Resolução do desafio: criando um sistema bancário com Python

saldo = 0
saque = 0
deposito = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUE = 500
menu ="""
Seja bem vindo! O que deseja realizar hoje?
[1]Saque
[2]Depósito
[3]Consultar extrato
[4]Sair
"""
opcao = 0

while True:
     opcao = int(input(menu))
     #saque
     if opcao == 1 and numero_saques < 3:
         saque = int(input("qual valor você deseja sacar?"))
         if saque <= saldo and saque <= 500 and saque > 0: 
             print("saque de realizado com sucesso!")
             numero_saques += 1
             saldo -= saque
             extrato.append(f"Saque de ------- R${saque}")
         elif saque > saldo:
             print("saldo insuficiente")
         elif saque <= 0:
             print("valor inválido")         
         elif saque > 500:
             print("o limite máximo para o saque é de R$500, tente novamente")
     #saque após o limite diário ser excedido
     elif opcao == 1 and numero_saques == 3:
         print("o seu limite diário de saques foi atingido")   
     #depósito
     elif opcao == 2:
         deposito = int(input("informe o valor do depósito"))
         if deposito > 0:
             saldo += deposito
             extrato.append((f"Depósito de ---- R${deposito}"))
         elif deposito <= 0:
                 print("valor inválido")
     #extrato
     elif opcao == 3:
         extrato_print = '\n'.join(extrato)
         print(extrato_print)
         print(f"seu saldo atual é R${saldo}")
     #encerramento do programa
     elif opcao == 4:
         break
     #opção inválida
     else:
         print("operação inválida")
