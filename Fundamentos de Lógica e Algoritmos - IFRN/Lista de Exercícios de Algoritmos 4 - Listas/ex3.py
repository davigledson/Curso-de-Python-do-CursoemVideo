'''Crie um programa que sorteie 10 números entre 1 e 100 e guarde-os numa lista. Ordene
a lista em ordem crescente e imprima na tela os valores sorteados.
'''
from random import randint
lista=[]
cont=0
while cont<10:
    cont+=1
    sorteado=randint(0,100)
    print(f'O {cont}° sorteado é {sorteado}')
    lista.append(sorteado)
print(lista)
