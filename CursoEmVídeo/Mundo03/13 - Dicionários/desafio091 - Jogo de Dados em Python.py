
dic={'Jogador1':0,'Jogador2':0,'Jogador3':0,'Jogador4':0}
dic['Jogador1']=2
diclist={}
from random import randint
for c in range(1,5):
    sorteado=randint(1,6)
    dic[f'Jogador{c}']=sorteado

print(dic)
print(sorted(dic.values()))

for k,v in dic.items():
    print(f'{k} tirou {v}')

from operator import itemgetter
ranking=sorted(dic.items(), key=itemgetter(1),reverse=True)
print(ranking)
print('='*20,'RANKING DOS JOGADORES','='*20)
cont=0

for k,v in  ranking:
    cont+=1
    print(f'        {cont}° lugar = {k} com {v} pontos')

print('===== EM FORMA DE LISTA =====')

'''OU'''
for k,v in enumerate(ranking) :

    print(f'        {k+1}° lugar = {v[0]} com {v[1]} pontos')




