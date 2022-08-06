sorteio=[]
lista=[]
j=int(input('Quantos jogos você quer que eu sorteie?'))
from random import randint
for d in range(0,j):
    for c in range(0,6):
        s=randint(0,60)
        sorteio.append(s)
    lista.append(sorteio[:])
    sorteio.clear()

for i in range(0,j):
    print(f'Jogo {i+1} = {lista[i]}')
