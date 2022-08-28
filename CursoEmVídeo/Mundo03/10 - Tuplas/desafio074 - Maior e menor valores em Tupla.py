from random import randint
cont=0
n1=n2=n3=n4=n5=0
n=' '
for c in range(0,5):

    n = randint(1, 10)

    cont += 1
    if cont == 1:
        n1 = n
    if cont == 2:
        n2 = n
    if cont == 2:
        n2 = n
    if cont == 3:
        n3 = n
    if cont == 4:
        n4 = n
    if cont == 5:
        n5 = n
trufa=(n1,n2,n3,n4,n5)
mi=min(trufa)
ma=max(trufa)
print(f' os numeros sorteados foram {trufa}')
print(f'o valor mínimo sorteado foi o {mi} e o máximo foi o  {ma}')
print('=='*20,'OUTRA FORMA','=='*20)

#OUTRA FORMA
numeros = randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10)
print(f'o valor mínimo sorteado foi o {min(numeros)} e o máximo foi o  {max(numeros)}')

print(f'Os valores sorteados foram:',end='')
for c in numeros:
    print(f' {c}',end='')

