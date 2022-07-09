termo=int(input('Digite o 1° termo:'))
razao=int(input('Digite a Razão:'))
contador=1
mais=10
total=0
while mais !=0:
    total += mais
    while contador<=total:
        print(f'{termo}')
        termo += razao
        contador += 1


    print('PAUSA')
    mais = int(input('Quantos Termos Você quer mostrar a mais?'))
print(f'Progressão finaliza com {total} Termos totais')

