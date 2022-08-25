'''Crie um programa que o usuário digita os dados de duas listas com 3 elementos cada.
Depois crie uma terceira lista com a junção dos elementos das outras duas. Imprima a nova
lista.'''
lista=[]
lista_alternativa=[]
lista1=[]
lista2=[]

for c in range(1,4):
    valor=int(input(f'{c}° Valor:'))
    lista1.append(valor)
for c in range(1,4):
    valor=int(input(f'{c}° Valor:'))
    lista2.append(valor)
lista.append(lista1)
lista.append(lista2)
print(lista1)
print(lista2)
print(lista) #Assim

for c in lista1:
    lista_alternativa.append(c)
for c in lista2:
    lista_alternativa.append(c)
print(f'Resposta alternativa = {lista_alternativa}')
