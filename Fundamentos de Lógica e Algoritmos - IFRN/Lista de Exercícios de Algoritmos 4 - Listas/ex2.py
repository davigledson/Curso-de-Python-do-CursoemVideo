'''Crie um programa em que o usuário digite 10 valores em uma lista e depois imprima a
lista.'''
cont=1
lista=[]
while cont <=10:

    n=input(f'Digite o {cont}° valor:')
    lista.append(n)
    cont+=1
print(lista)
