def contador(i,f,p):


    if p ==0:
        p=1
    if i<f and p>0:
        for c in range(i,f+1,p):
            print(f'{c} ', end='')
        print('FIM')

    if i<f and p<0:
        for c in range(f,i-1,p):
            print(f'{c} ', end='')
        print('FIM')



    lista = []
    if i>f and p>0:

        for c in range(f,i+1,p):
            lista.append(c)


        for c in lista[::-1]:
            print(f'{c} ',end='')
        print('FIM')

    if i > f and p < 0:

        for c in range(i, f-1, p):
            lista.append(c)

        for c in lista:
            print(f'{c} ', end='')
        print('FIM')

inicio=int(input('Inicio:'))
fim=int(input('Fim:'))
passo=int(input('Passo:'))

contador(1,10,0)
contador(10,1,2)
contador(inicio,fim,passo)

print('FOR','='*20)
for c in range(inicio,fim,passo):
    print(f'{c} ',end='')
print()
