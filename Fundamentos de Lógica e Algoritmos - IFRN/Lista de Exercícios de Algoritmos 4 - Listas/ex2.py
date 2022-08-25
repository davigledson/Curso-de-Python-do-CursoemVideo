'''Crie um programa em que o usuário digite 10 valores em uma lista e depois imprima a
lista.'''
cont=0
lista=[]
while cont <10:

    n=input('Digite um valor:')
    lista.append(n)
    cont+=1
print(lista)
