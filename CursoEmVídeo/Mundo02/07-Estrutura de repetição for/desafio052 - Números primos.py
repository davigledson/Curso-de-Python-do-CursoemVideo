n1=int(input('digite um numero:'))
contador=0
contint=0
for c in range(1,n1+1):

    contador+=1
    if n1%c ==0:
        contint+=1

if contint>=3:

    print(f'{n1}Não é um numero primo')


print(f'{n1} é divisivel por {contint} numeros')
if contint==2:
    print(f'{n1} e um numero primo pois é divisivel 1 e por ele mesmo')
