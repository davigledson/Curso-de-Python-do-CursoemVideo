print('R para residencial')
print('C para Comercial')
print('I para industrial')
ins=input('Digite sua qual seu tipo de instalação:').lower()
kw=float(input('Quantidade de kWh consumidas:'))

if ins== 'r':
    if kw<=500:
        print(f'Sua conta será de R${kw*0.40}')
    if kw>500:
        print(f'Sua conta será de R${kw*0.65}')

if ins== 'c':
    if kw<=1000:
        print(f'Sua conta será de R${kw*0.55}')
    if kw>1000:
        print(f'Sua conta será de R${kw*0.60}')

if ins== 'i':
    if kw<=5000:
        print(f'Sua conta será de R${kw*0.55}')
    if kw>5000:
        print(f'Sua conta será de R${kw*0.60}')
