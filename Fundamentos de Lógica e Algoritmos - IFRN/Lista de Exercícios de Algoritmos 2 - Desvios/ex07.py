alt=float(input('informe sua altura:').replace(',','.'))

print('M para macho')
print('F - para femea')
sex=input('informe seu sexo:').lower()



if sex == 'm':
    print(f'seu peso ideal seria de {(72*alt)-58}')

if sex == 'f':
    print(f'seu peso ideal seria de {(62.1*alt)-44.7}')