n1=int(input('Digite sua 1° nota:'))
n2=int(input('Digite sua 2° nota:'))
n3=int(input('Digite sua 3° nota:'))
n4=int(input('Digite sua 4° nota:'))

eq=(n1+n2+n3+n4)/4
if eq>=6:
    print('você foi APROVADO')
if eq<6:
    print('voce foi REPROVADO')