
n1=int(input('digite o numero do termo:'))

ultimo=1
penultimo=1
if n1==1 or n1==2:
    print('1')
else:
    count=3
    while count<=n1:
        termo= ultimo + penultimo
        penultimo = ultimo
        ultimo=termo
        count+=1
        print(f'{count-1}°Termo = {termo}')

