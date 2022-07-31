lista=[]
val=input('Digite uma expressão:')
lista.append(val)
cont9=0
cont0=0

for pos,valores in enumerate(lista):
    for v in valores:


        if '(' in v:
            cont9+=1
        if ')' in v:
            cont0+=1


if cont9 == cont0:
    print('Sua expressão está valida!')
else:
    print(f'Sua expressão está invalida!')