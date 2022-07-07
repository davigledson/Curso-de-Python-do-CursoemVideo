'''for c in range(0,11):
    print(c)
print('Fim')'''

print(20*'=','A BASE', 20*'=')
c = 1
while c <= 10:
    print(c)
    c = c + 1
    '''or c += 1'''


print('FIM')
print(20 * '=', 'COMO PARAR', 20 * '=')
n = 1
while n != 0:
    n = int(input('Digite um Valor:'))
print('FIM')

print(20*'=','ESCOLHAS', 20*'=')
r = 's'
while r == 's':
    input('Digite um Valor:')
    r = input('Quer Continuar? [S/N]').lower()
print('FIM')

print(20*'=','NùMEROS PARES E IMPARES', 20*'=')
par = impar = 0
g=1
while g != 0:
    g = int(input('Digite um valor:'))
    if g != 0:
        if g % 2 ==0:
            par+=1
        else:
            impar+=1
print(f'Voce digitou {par} pares e {impar} números ímpares')