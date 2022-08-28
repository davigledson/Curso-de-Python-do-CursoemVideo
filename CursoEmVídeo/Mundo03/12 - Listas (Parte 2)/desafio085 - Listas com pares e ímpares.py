lista=[] #podia ter feito lista=[[],[]] tbm
impar=[]
par=[]
for c in range(0,7):
    valor=int(input('Digite um valor:'))
    if valor %2==0:
        par.append(valor)
    if valor %2==1:
        impar.append(valor)
lista.append(impar[:])
lista.append(par[:])

print(f'Lista dos impares: {impar}')
print(f'Lista dos pares: {par}')
print(f'Lista dos pares e ímpares: {lista}')
print(f'Lista completa em ordem crescente: {sorted(lista[0]),sorted(lista[1])}')