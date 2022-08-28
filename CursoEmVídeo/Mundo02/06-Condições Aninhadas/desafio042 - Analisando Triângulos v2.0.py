print('analisador de triangulos V2.0')
n1=float(input('digite o 1° complemento:'))
n2=float(input('digite o 2° complemento'))
n3=float(input('digite o 3° complemento'))

eq=n1!= n2 != n3

if n1< n2+n3 and n2<n1+n3 and n3<n2+n1:
    print('SIM, dar para formar um triangulo. ')
    if n1 !=n2 !=n3:
        print('um triangulo ESCALENO - onde todos os lados são diferentes, precisamente.')
    if n1==n2 != n3 or n1==n3 !=n2  or n2==n3 !=n1:
        print('um triangulo ISÓCELES - onde dois lados são iguais, precisamente')
    if n1 == n2 ==n3:
        print('um triangulo EQUILÁTERO - todos todos os lados são iguais, precisamente')
else:
    print('Não dar para forma um triangulo!')