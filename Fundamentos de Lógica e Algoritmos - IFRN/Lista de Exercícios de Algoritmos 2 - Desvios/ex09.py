hr=float(input('Digite o numero de horas trabalhadas por semana:'))
hrs=hr*12.50
ex=(hr-40)*18.40

if hr>40:

    print(f'seu pagamento será de R${hrs} e de R${ex} por hora extra')
    print(f'totalizando R${hrs+ex}')

if hr<=40:

    print(f'seu pagamento será de R${hrs} ')
