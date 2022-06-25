print('Digite em CM')
alt=float(input('digite sua altura:').replace(',','.'))


print('Digite em Kg')
pes=float(input('digite seu peso:'))
imc=pes/(alt*alt)
print(f'seu IMC é {imc:.1f} ')
if imc< 18.5:
    print('abaixo do peso')
elif 25>imc>18.5:
    print('peso ideal')
elif 30>imc>25:
    print('Sobrepeso')
elif 40>imc>30:
    print('Obesidade')
elif imc>40:
    print('Obesidade Mórbida')
