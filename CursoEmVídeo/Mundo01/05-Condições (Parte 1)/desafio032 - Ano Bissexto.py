from datetime import date

n1=int(input('\033[32m em qual ano você está:'))

print('se você colocar 0 e usa o modulo datetime e usa o date'
      'o computador pega o numero configurado na maquina ')

if n1==0:
    n1=date.today().year

if n1 % 4 ==0 and n1 %100 !=0 or n1 %400==0:
    print(f'seu {n1} é um ano bissexto')
else:
    print(f'seu {n1} é um ano normal')


