'''Faça um programa que permita ao usuario palpitar quem é o impostor,
 sendo que se o palpite estiver errado,o participante selecionado será eliminado
 e em cada rodada o impostor eliminará um participante'''
lista=['Davi Gledson','Carlos Eduardo','Maria Yashin','Gabriel Firmino','Pedro Ricardo','Nicassio Monteiro','Rafaela Ficheira','Maedson Calvagar']

from random import randint
from time import sleep

escolha_do_impostor=randint(0,len(lista)-1)
impostor=lista[escolha_do_impostor]
print('==='*20)
print(f'Há um impostor entre nós')
print('==='*20)
posicao_do_impostor=0
while True:
    if impostor in lista:
        posicao_do_impostor=lista.index(impostor)

    escolha_da_morte=randint(0,len(lista)-1)
    while escolha_da_morte == posicao_do_impostor:
        escolha_da_morte = randint(0, len(lista) - 1)
    morte = lista[escolha_da_morte]

    print(f'O impostor matou {morte}')
    lista.remove(morte)
    sleep(1)

    print(f'Os Sobreviventes são {lista}')
    sleep(1)

    for pos,d in enumerate(lista) :
        print(f'[{pos}] - {d}')

    usu=int(input(f'Quem é o impostor? [digite de 0 até {len(lista)-1}]:'))





    if lista[usu] ==impostor:
        print('=' * 20)
        frase_lenta = f'{impostor} era o Impostor'
        for i in frase_lenta:
            print(i, end='')
            sleep(.1)
        print()
        print('=' * 20)
        print(f'Parabens! VOCÊ GANHOU!')
        break
    else:
        frase_lenta1=f'{lista[usu]} não era o impostor!'
        for i in frase_lenta1:
            print(i,end='')
            sleep(.1)
        print()
        lista.remove(lista[usu])

    if len(lista) <=2:
        print('='*20)

        print(f'{impostor} era o Impostor')
        print('=' * 20)
        print(f'VOCÊ PERDEU!')
        break
    sleep(1)
