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






