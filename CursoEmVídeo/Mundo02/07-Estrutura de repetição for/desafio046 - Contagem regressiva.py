# Estrutura de repetição for
for a in range(0,5):
    print(a)

print('Fim')

for b in range(0,7,2):
    print(b)

n=int(input('digite um numero:'))
for c in range(0,n):
    print(c)
i=int(input('Inicio:'))
f=int(input('Final:'))
p=int(input('Passo:'))

for d in range(i,f+1,p):
    print(d)


print('contagem regressiva de:')
for e in range(10,-1,-1):
    import time
    print(e)
    time.sleep(1)
print('BOOM!!!')
