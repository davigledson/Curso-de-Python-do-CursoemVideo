lista=[]
impar=[]
par=[]
while True:
    val=int(input('Digite um valor:'))
    lista.append(val)

    esc=' '
    while esc not in 'SsNn':
        esc=input('Quer Continuar?').lower()[0]
    if esc =='n':
        break

for pos, valores in enumerate(lista):
    if valores %2 ==1:
        impar.append(valores)

    if valores % 2 ==0:
        par.append(valores)

print(f'A lista completa é {lista}')
print(f'a lista dos ímpares é {impar}')
print(f'A lista dos pares {par}')