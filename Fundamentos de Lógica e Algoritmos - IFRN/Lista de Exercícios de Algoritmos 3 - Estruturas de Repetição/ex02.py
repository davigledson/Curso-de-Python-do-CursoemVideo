n=int(input('Digite um numero:'))
i=int(input('Digite o Inicio da tabuada:'))
f=int(input('Digite o fim da tabuada:'))

for c in range(i,f):
    print(f'{n} X {c} = {n*c}')