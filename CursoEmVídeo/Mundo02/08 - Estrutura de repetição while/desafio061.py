n1=int(input('Digite o 1° termo:'))
r=int(input('Digite a Razão:'))
contador=0

while contador<10:
    contador+=1
    a=contador*(n1*r)
    print(f'{contador}° termo =  {a}')