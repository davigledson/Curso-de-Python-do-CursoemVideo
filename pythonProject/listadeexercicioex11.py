n=input('Digite seu nome:')
c=int(input('Digite o numero de carros vendidos:'))
v=int(input('Digite o valor total das vendas:'))

sl=500+c*50+ v*5/100
print(f'o salário de {n} será de R${sl}')