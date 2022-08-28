n1=int(input('digite um número para ver sua tabuada:'))
print('multiplicação:')
print('='*60)
for m in range(1,11):
    print(f'{m} * {n1}= {n1*m}')
print('='*60)
print('divisão:')
for d in range(1,11):
    print(f'{d} / {n1} = {d/n1}')
print('='*60)
print('adição:')
for a in range(1,11):
    print(f'{a} + {n1} = {n1+a}')
print('subtração:')
print('='*60)
for s in range(1,11):
    print(f'{s} - {n1} = {s-n1}')