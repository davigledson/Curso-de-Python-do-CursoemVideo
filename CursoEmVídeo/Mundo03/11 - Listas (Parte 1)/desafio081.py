lista=[]
n5=[]
cont=0
while True:
    val=int(input('Digite um valor:'))
    lista.append(val)


    esc = ' '
    while esc != 'n' and esc !='s':
        esc=input('Quer Continuar [S/N]:').lower()[0]
    if esc == 'n':
        break


print(lista)
print(f'A contagem de valores na lista e de {len(lista)}')

for pos, valores in enumerate(lista):
    if 5 == valores:

        n5.append(pos)

if 5 in lista:
    print(f'O valor 5 estar na lista na posição {n5}')
else:
    print(f'O valor 5 não estar na lista')

lista.sort(reverse=True) # não funciona dentro de print
print(f'A ordem decrescente da lista é {lista}')