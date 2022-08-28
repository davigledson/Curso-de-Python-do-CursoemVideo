n=int(input('digite um numero de 0 a 9999:'))
n1=str(input('digite de novo para o teste 2:'))
uni=print('unidades:',n1[3])
dez=print('dezenas:',n1[2])
Qcen=print('centenas:',n1[1])
mil=print('milhar',n1[0])

#jeito correto de fazer com o que aprendeu áte aqui
print('feito do jeito matemático')

print('unidades',n // 1 % 10)
print('dezenas', n // 10 % 10)
print('centenas', n // 100 % 10)
print('milhar', n // 1000 % 10)

print('jeitinho brasileiro de fazer')
n2=str(n + 10000)
print('unidades',n2[4])
print('dezenas', n2[3])
print('centenas', n2[2])
print('milhar',n2[1])
