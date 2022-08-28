a=float(input('digite sua 1°Nota:'))
b=float(input('digite sua 2°nota:'))
eq=(a+b)/2

if eq >= 6:
    print('Parabens, você foi aprovado!')
elif 5<=eq <6:
    print('você ficou em recuperação!')
elif eq < 5:
    print('Infelizmente você foi reprovado. Estude mais!')