cas=float(input('Digite o valor da casa:'))
sal=float(input('Digite seu salario:'))
anos=float(input('Digite a quantidade de anos a pagar:'))

mes=anos*12
cs=cas/mes
s30=sal*30/100

print(f'valor da prestação:R${s30} por mes')


if s30<=cs:
    print('o valor e INSUFICIENTE pra compra essa casa')
    print(f'valor seria de R${cs:.2f} por {mes} meses')
if s30>=cs:
    print('o valor do seu salario e SUFICIENTE pra compra essa casa')
    print(f'valor da prestação é de :R${cs:.2f} por {mes} meses')