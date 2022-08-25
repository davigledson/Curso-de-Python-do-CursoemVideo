'''Crie um programa em que o usuário digite 10 valores em uma lista. Ao final o programa
deve informar o maior e o menor valor digitado e suas posições na lista.'''
cont=0
lista=[]
while cont<10:
    cont+=1
    valor=int(input('Digite um valor:'))
    lista.append(valor)
print(lista)
print(f'O menor valor digitado na lista foi o {min(lista)} na posição {lista.index(min(lista))}')
print(f'O maior valor digitado na lista foi o {max(lista)} na posição {lista.index(max(lista))}')
