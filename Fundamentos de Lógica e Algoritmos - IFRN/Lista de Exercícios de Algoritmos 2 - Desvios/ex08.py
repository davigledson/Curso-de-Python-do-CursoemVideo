pei=float(input('Digite o peso dos peixes em Kg:'))

if pei>50:
    print(f'a multa será de R${(pei-50)*4}')
if pei<=50:
    print(f'nenhuma multa')