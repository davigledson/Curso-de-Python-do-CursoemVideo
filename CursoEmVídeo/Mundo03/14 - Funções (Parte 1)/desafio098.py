def contador(i,f,p):


    if p ==0:
        p=1

    if i<f and p>0:
        print(f'Contagem de {i} até {f} contando de {p}  em {p}')
        for c in range(i,f+1,p):
            print(f'{c} ', end='')
        print('FIM')

    if i<f and p<0:
        print(f'Contagem de {i} até {f} contando de {p}  em {p}')
        for c in range(i,f+1,-p):
            print(f'{c} ', end='')
        print('FIM')



    lista = []
    if i>f and p>0:
        print(f'Contagem de {i} até {f} contando de {p} em {p}')
        for c in range(f,i+1,p):
            lista.append(c)


        for c in lista[::-1]:
            print(f'{c} ',end='')
        print('FIM')

    if i > f and p < 0:
        print(f'Contagem de {i} até {f} contando de {p} em {p}')
        for c in range(i, f-1, p):
            lista.append(c)

        for c in lista:
            print(f'{c} ', end='')
        print('FIM')
def mostralinha():
    print('-=-'*20)
inicio=int(input('Inicio:'))
fim=int(input('Fim:'))
passo=int(input('Passo:'))

mostralinha()
contador(1,10,0)
mostralinha()

contador(10,0,2)
mostralinha()

contador(inicio,fim,passo)

print('FOR','='*20)
for c in range(inicio,fim,passo):
    print(f'{c} ',end='')
print()
