print('Hambúrguer................. R$ 3,00')
print('Cheeseburger............... R$ 2,50 ')
print('Fritas.........................R$ 2,50')
print('Refrigerante................. R$ 1,00')
print('Milkshake..................... R$ 3,00')
hamburguer=3
cheeseburger=2.50
fritas=2.50
refrigerante=1.00
milkshake=3

a=input('digite o nome do produto que você consumiu:').replace('ú','u').lower()

if 'hamburguer' in a:
    b=int(input('digite a quantidade do produto que você consumiu:'))
    print(f'sua conta será de R${hamburguer*b}')

if 'cheeseburger' in a:
    b=int(input('digite a quantidade do produto que você consumiu:'))
    print(f'sua conta será de R${cheeseburger*b}')

if 'fritas' in a:
    b=int(input('digite a quantidade do produto que você consumiu:'))
    print(f'sua conta será de R${b*fritas}')

if 'refrigerante' in a:
    b=int(input('digite a quantidade do produto que você consumiu:'))
    print(f'sua conta será de R${fritas*b}')

if 'milkshake' in a:
    b=int(input('digite a quantidade do produto que você consumiu:'))
    print(f'sua conta será de R${b*milkshake}')
else:
    print('produto inexistente')

