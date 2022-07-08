n1=int(input('Digite o 1° numero:'))
n2=int(input('Digite o 2° numero:'))
som=n1+n2
sub=n1-n2
mult=n1*n2
div= n1/n2
maior=max(n1,n2)
menor=min(n1,n2)
print('[1] Somar')
print('[2]Subtrair')
print('[3] Multiplicar')
print('[4] Dividir')
print('[5] Maior')
print('[6] Novos números')
print('[7] Sair do programa')




p=1
while p != 7:
    p = int(input('Escolha uma Operação para Realizar:'))
    if p==1:
        print(som)
    if p==2:
        print(sub)
    if p==3:
        print(mult)
    if p==4:
        print(div)
    if p==5:
        print(f'{maior} é maior que {menor}')
    if p==6:
        n1 = int(input('Digite o 1° numero:'))
        n2 = int(input('Digite o 2° numero:'))

