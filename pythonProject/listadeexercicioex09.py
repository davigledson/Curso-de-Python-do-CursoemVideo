cf = int(input('digite o custo de preço da fabrica:'))
dis = 12 * cf / 100
imp = 45 * cf / 100
com = dis+imp
print(f'preço com 12% do distribuidor será R${dis+cf}')
print(f'preço com 45% dos impostos será R${imp+cf}')
print(f'o novo preço com os impostos de ambos será R${com+cf}')