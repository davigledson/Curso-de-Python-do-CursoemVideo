
quant=0
soma=0
maior=0
menor=0
rest='s'
while rest in 'Ss':
    n1 = int(input('digite o numero a ser somado:'))
    quant+=1
    soma+=n1

    rest = input('Quer continuar? [S/N]:').lower().strip()[0]

    if quant==1:
        maior=menor=n1
    else:
        if n1>maior:
            maior=n1

        if n1<menor:
            menor=n1


media = (soma) / (quant)
print(f'o contador de numeros digitados foi de: {quant}')
print(f'a soma dos numeros digitados foi de: {soma}')
print(f'A media dos numeros digitados foi de: {media}')

print(f'O maior valor digitado foi de: {maior}')
print(f'O menor valor digitado foi de: {menor}')