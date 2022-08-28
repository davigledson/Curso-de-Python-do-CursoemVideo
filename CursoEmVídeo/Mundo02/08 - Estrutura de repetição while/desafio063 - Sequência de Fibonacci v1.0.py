print('='*30)
print('Sequencia de Fibonacci')
print('='*30)

n1=int(input('digite o numero do termo:'))

print('~~'*15)
ultimo=0
penultimo=1

count=0
while count<n1:
    termo= ultimo + penultimo
    penultimo = ultimo
    ultimo=termo
    count+=1
    print(f'{count}°Termo = {termo}')

