n1 =input('digite uma frase:').replace(' ', '')
contador=0
le=len(n1)

invertida=n1[::-1]
print(invertida)
print('='*50)

for c in range(1,le-1):
    contador += 1
if n1 == invertida:
    print('É um um palíndromo')
    print(f'o inverso de {n1} é {invertida} portando, é um palíndromo')
else:
    print('Não e um palíndromo')
    print(f'o inverso de {n1} é {invertida} portando, não é um palíndromo')

