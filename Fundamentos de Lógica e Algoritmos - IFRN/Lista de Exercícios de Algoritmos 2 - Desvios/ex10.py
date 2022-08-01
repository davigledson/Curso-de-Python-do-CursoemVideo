sal=float(input('Digite seu salario:'))
if sal<=1000:
    print(f'o novo salario será de R${sal*15/100+sal}')
if sal<=2000:
    print(f'o novo salario será de R${sal*10/100+sal}')
if sal<=3000:
    print(f'o novo salario será de R${sal*5/100+sal}')
if sal>3000:
    print(f'o novo salario será de R${sal*2.5/100+sal}')