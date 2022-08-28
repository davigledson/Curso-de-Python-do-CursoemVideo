# programa para calcular valor a ser pago por um produto





a=float(input('Preços das compras:'))

print('Ótimo, escolha a opção de pagamento')
print(f'1- A vista,com dinheiro ou cheque- 10% de desconto:- {(a*10/100)-a}')
print(f'2- A vista, no cartão - 5% de desconto: - R${a-(a*5/100)}')
print(f'3- Em até 2x vezes no cartão - de R${a/2}')
print(f'4- Em até 3x vezes ou mais no cartão - 20% de juros:R$ {(a*20/100)+a}')
b=input('Digite 1,2,3 ou 4:')
print('Ótimo, pedido encaminhado:')



if '1' in b:
    print(f'Preço final:{(a*10/100)-a}')
if '2' in b:
    print(f'Preço final:{a-(a*5/100)}')
if '3' in b:
    print(f'Preço final{a} dividido em duas parcelas de R${a/2}')

if '4' in b:

    a3 = int(input('quantas parcelas vão ser?'))
    print(f'Preço final: R${(a*20/100)+a} dividido em {a3} parcelas de de R$ de {((a*20/100)+a)/a3}')
