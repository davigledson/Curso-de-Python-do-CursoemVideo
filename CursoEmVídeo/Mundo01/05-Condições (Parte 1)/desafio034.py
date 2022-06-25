n1=float(input('\033[0;37;40m digite o salário:'))
#print('se o salário for superior a R$1.250,00 o aumento será de 10%. \n Para os inferiores  ou iguais será de 15%')
a=(n1 /100) *10
b=n1+a

c=(n1/100)*15
d=n1+c

if n1>= 1250:
    print(f'seu aumento será de {a}, seu novo salário será {b}')
else:
    print(f'seu aumento será de {c}, seu novo salário será {d}')