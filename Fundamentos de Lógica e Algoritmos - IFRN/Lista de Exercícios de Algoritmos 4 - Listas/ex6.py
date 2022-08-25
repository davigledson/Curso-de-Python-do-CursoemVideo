'''Crie um programa que sorteie números aleatórios entre 1 e 100. Preencha uma lista com
20 elementos *diferentes*, organize em ordem decrescente e imprima na tela.'''
from random import randint
lista=[]
cont=0
while cont<20:
    s=randint(0,100)
    cont+=1
    lista.append(s)
print(lista)
lista.sort(reverse=True)
print(f'lista reversa= {lista}')

