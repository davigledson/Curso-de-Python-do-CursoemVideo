'''Crie um programa que sorteia 20 números e guarda-os numa lista. Permita que o usuário
faça pesquisas na lista. Se o número pesquisado existe na lista, informe a sua posição. Se o
elemento não existe, mostre uma mensagem informando. O usuário poderá repetir novas
pesquisas quantas vezes quiser.
'''
lista=[]
from random import randint
for c in range(1,21):
    sorteado=randint(0,100)
    lista.append(sorteado)

print(lista)

while True:
    pesq=int(input('Qual numero deseja pesquisa na lista?'))
    if pesq in lista:
        print(f'O numero {pesq} está na lista na posição {lista.index(pesq)}')
    else:
        print('O numero não existe na lista!')
    usuario=input('Quer Continuar[S/N]:').lower()[0]
    if usuario=='n':
        break

