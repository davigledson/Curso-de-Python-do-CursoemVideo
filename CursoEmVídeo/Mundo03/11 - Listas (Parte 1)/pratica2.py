#valores=list() da pra criar lista assim
valores=[] # e assim
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(f'{v}...')

for c,v1 in enumerate(valores): # o enumerate pega tanto a chave quanto o valor
    print(f'na posição {c} encontrei o valor {v1}!')
print('cheguei ao final da lista.')



valores1=[]
for cont in range(0,5):#lendo valores pelo teclado e colocando na lista
    valores1.append(int(input('digite um valor:')))

for c1,v2 in enumerate(valores1):
    print(f'na posição {c1} encontrei {v2}')
