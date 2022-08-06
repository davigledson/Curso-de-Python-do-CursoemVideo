matriz=[]
lista0=[]
lista1=[]
lista2=[]
par=[]
for c0 in range(0,3):
    v0=int(input(f'Digite um valor para a posição [ 0 , {c0} ]:'))
    lista0.append(v0)

    if v0 %2==0:
        par.append(v0)

for c1 in range(0,3):
    v1=int(input(f'Digite um valor para a posição [ 1 , {c1} ]:'))
    lista1.append(v1)

    if v1 %2==0:
        par.append(v1)

for c2 in range(0,3):
    v2=int(input(f'Digite um valor para a posição [ 2 , {c2} ]:'))
    lista2.append(v2)

    if v2 %2==0:
        par.append(v2)

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
print()

somapar=0

for p in par:
    somapar+=p
print(f'A lista dos numeros pares é {par} é a soma deles é {somapar}')
soma2=0

n1=matriz[0][2]
n2=matriz[1][2]
n3=matriz[2][2]


print(f'A soma dos numeros da terceira coluna é de {n1+n2+n3}')

ma=max(matriz[1])
print(f'O valor maximo da 2° linha é {ma}')