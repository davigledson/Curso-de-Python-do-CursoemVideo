print('='* 20)
print('Analisador de Triangulos V1.0')
print('='* 20)


n1=float(input('\033[0;34;40m digite o 1°comprimento:'))
n2=float(input('\033[0;35;40m digite o 2° comprimento:'))
n3=float(input('\033[0;36;40m digite o 3° comprimento:'))

if n1 < n2 + n3 and n2 < n1+ n3 and n3< n1 + n2:
    print('SIM, DAR para forma um triangulo')
else:
    print('NÃO, não dar para forma um triangulo')
