a=int(input('\033[34m digite o primeiro número:'))
b=int(input('digite o segundo número:'))
c=int(input('digite o terceiro número:'))

d=max(a,b,c)
e=min(a,b,c)

print(f'{d} é o maior número')
print(f'{e} é o menor número')

r=(a,b,c)
print('em ordem crescente ',(sorted(r)))

#usando o if
menor=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

print(f'o menor valor digitado foi {menor}')

maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

print(f'o maior valor digitado foi {maior}')
