matriz=[[0,0,0,],[0,0,0],[0,0,0]]
'''lista0=[]
lista1=[]
lista2=[]
for c0 in range(0,3):
    v0=int(input(f'Digite um valor para a posição [ 0 , {c0} ]:'))
    lista0.append(v0)
for c1 in range(0,3):
    v1=int(input(f'Digite um valor para a posição [ 1 , {c1} ]:'))
    lista1.append(v1)
for c2 in range(0,3):
    v2=int(input(f'Digite um valor para a posição [ 2 , {c2} ]:'))
    lista2.append(v2)

matriz.append(lista0[:])
matriz.append(lista1[:])
matriz.append(lista2[:])



print('='*20,'MATRIZ','='*20) #matriz normal
print(matriz[0])
print(matriz[1])
print(matriz[2])

#matriz com []
for m0 in matriz[0]:
    print(f'[ {m0} ]',end='')
print()
for m1 in matriz[1]:
    print(f'[ {m1} ]',end='')
print()
for m2 in matriz[2]:
    print(f'[ {m2} ]',end='')
print()'''

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um valor para a posição [ {l} ] [ {c} ]: '))

for l in range(0,3):
    for  c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()