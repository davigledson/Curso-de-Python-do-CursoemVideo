print('=='*20)
print('BANCO CEV')
print('=='*20)
saque=int(input('Qual será o valor a ser sacado?'))
total=saque
ced=50
tolced=0
while True:
    if total>=ced:
        total-=ced
        tolced+=1
    else:
        if tolced>0:
            print(f'o total de {tolced} cédulas de R${ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        tolced=0
        if total==0:
            break












