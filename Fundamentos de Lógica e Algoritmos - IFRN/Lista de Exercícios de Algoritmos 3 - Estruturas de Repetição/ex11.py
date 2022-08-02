cont=0
maior=menor=0

while True:
    cont += 1
    n = int(input('Digite um numero:'))

    if cont==1:
        maior=menor=1
    else:
        if cont ==1 or maior<n :
            maior=n
        if cont==1 or menor>n:
            menor=n


    if n<=0:
        break

print(f'o maior numero digitado é {maior} e o menor é {menor}')