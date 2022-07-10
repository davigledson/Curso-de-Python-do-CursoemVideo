n1=0
count=1
soma=0
while n1!= 999:
    count+=1
    soma+=n1
    n1 = int(input('digite o numero a ser somado:'))
print(f'o contador de numeros digitados foi de: {count-2}')
print(f'a soma dos numeros digitados foi de {soma}')