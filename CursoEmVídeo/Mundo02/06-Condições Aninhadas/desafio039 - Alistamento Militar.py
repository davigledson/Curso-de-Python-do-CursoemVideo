#programa para ver alistamento
import datetime
n=int(input('digite seu ano de nascimento:'))
n1=datetime.date.today().year
idade=n1-n

print(f'quaem nasceu em {n} tem {idade}')
if idade >18:
    print(f'seu ano de alistamento era em {n+18}')
elif idade <18:
    print(f'seu alistamento será em {n+18}')
elif idade== 18:
    print('seu alistamento será ainda esse ano')
