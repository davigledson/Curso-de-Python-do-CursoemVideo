lista=[]
dicionario={}

jogador=input('Nome do Jogador:')
dicionario['Jogador']=jogador

partidas=int(input('Quantas Partidas ele Jogou:'))
total_de_gols=0
for c in range(1,partidas+1):
    qg=int(input(f'Quantidade de gol na partida {c}:'))

    lista.append(qg)
    total_de_gols += qg


dicionario['Gols']=lista
dicionario['Total de Gols']=total_de_gols

print('=-=-='*30)

for k,v in dicionario.items():
    print(f'O campo {k} tem valor {v}')

print('=-=-='*30)
print(f'O jogador {jogador} jogou {partidas} partidas')
for pos,val in enumerate(lista):
    print(f'   => Na partida {pos+1} ele fez {val} gols')
print(f'Foi um total de {sum(dicionario["Gols"])} gols') # sum = soma




