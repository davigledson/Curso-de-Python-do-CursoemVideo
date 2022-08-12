'''Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Maior e Menor
[6] Novos números
[7] Sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1=int(input('Digite o 1° numero:'))
n2=int(input('Digite o 2° numero:'))
som=n1+n2
sub=n1-n2
mult=n1*n2
div= n1/n2
maior=max(n1,n2)
menor=min(n1,n2)




p=1
while p != 7:
    print('[1] Somar')
    print('[2] Subtrair')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Maior e Menor')
    print('[6] Novos números')
    print('[7] Sair do programa')
    print(40 * '=')
    p = int(input('Escolha uma Operação para Realizar:'))
    if p==1:
        print(f'o resultado e ',som)
    if p==2:
        print(f'o resultado e ',sub)
    if p==3:
        print(f'o resultado e ',mult)
    if p==4:
        print(f'o resultado e ',div)
    if p==5:
        print(f'{maior} é maior que {menor}')
    if p==6:
        n1 = int(input('Digite o 1° numero:'))
        n2 = int(input('Digite o 2° numero:'))
    if p != 1 and p !=2 and p!=3 and p!= 4 and p!=5 and p!=6 and p!= 7:
        print('Opção invalida! tente novamente')

print('Finalizando! Volte sempre!')