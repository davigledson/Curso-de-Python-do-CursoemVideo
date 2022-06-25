# programa para aprova emprestimo bancario para compra de uma casa
c=float(input('qual o valor da casa que pretende compra?'))
s=float(input('qual o seu salário?'))
a=int(input('em quantos anos você pretende paga?'))

n1=12 * a
n2= c/ n1
n3= s * 30 /100
import math

if n3< n2:
    print(f'infelizmente o valor do seu salário de {n2} é insuficiente para aprova esse financiamento')
elif c<=5000:
    print('o valor da casa e insuficiente para o requerimento do financiamento')
else:
    print(f'parabens seu financiamento foi aprovado, você ira pagar R${math.trunc(n2)} por {n1} meses')

