deposito=float(input('Digite o deposito inicial:'))
taxa=float(input('Digite a taxa de rendimento mensal:'))
saldo=deposito
for c in range(1,25):
    saldo=saldo+(saldo*(taxa/100))
    print(f'O saldo do mês {c} e R${saldo:.2f}')