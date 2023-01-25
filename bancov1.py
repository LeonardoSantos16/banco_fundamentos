extrato = ""
Usuario = {
    "Nome": "Leonardo",
    "Agencia": "323",
    "Conta": "corrente",
    "saldo": 0,
    "saques_diarios": 0
}
Menu = 0
while Menu != 4:
    Menu = int(input("1 - Deposito \n2 - Saque \n3 - Extrato\n4 - Sair \n"))
    if Menu == 1:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            extrato += f'valor adicionado + {valor:.2f} \n'
            Usuario["saldo"] += valor
        else:
            print("Não é possivél adicionar valor negativo")
    elif Menu == 2:
        valor = float(input("Digite o valor de saque: "))
        if valor < Usuario["saldo"] and valor <= 500 and Usuario["saques_diarios"] < 3:
            Usuario["saldo"] -= valor
            extrato += f'valor sacado - {valor:.2f} \n'
            Usuario["saques_diarios"] += 1
        else:
            print("Não é possivél sacar o dinheiro por falta de saldo")
    elif Menu == 3:
        if len(extrato) == 0:
            print("Não foram realizados movimentações")
        else:
            arredondar = round(Usuario["saldo"], 2)
            extrato += f'R$ {arredondar}'
            print(extrato)

print(Usuario)
