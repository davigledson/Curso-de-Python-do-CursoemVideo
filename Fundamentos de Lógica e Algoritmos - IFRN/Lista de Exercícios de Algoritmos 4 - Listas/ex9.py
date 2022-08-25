'''Modifique o programa 8 para que o usuário digite dois valores na pesquisa. O programa
percorre a lista procurando os dois ao mesmo tempo e diz qual dos dois valores foi
encontrado primeiro (mais próximo do início da lista). Dica: use um intervalo de sorteio
pequeno, com números entre 1 e 10, por exemplo.
'''
lista=[]
pos1=0
pos2=0
from random import randint
for c in range(1,21):
    sorteado=randint(0,10)
    lista.append(sorteado)

print(lista)

while True:
    pesq1=int(input('1° numero que deseja pesquisa na lista?'))
    pesq2 = int(input('2° numero que deseja pesquisa na lista?'))

    if pesq1 in lista:
        pos1=lista.index(pesq1)
    if pesq2 in lista:
        pos2=lista.index(pesq2)
    menor_posicao=min(pos1,pos2)

    print(f'O valor mais proximo do inicio da lista foi o {lista[menor_posicao]} na posição {menor_posicao}')
    usuario=input('Quer Continuar[S/N]:').lower()[0]
    if usuario=='n':
        break

