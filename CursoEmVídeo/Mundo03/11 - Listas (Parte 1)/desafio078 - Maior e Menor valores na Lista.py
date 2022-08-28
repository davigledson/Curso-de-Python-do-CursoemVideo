lista=[]
posicao_menor=[]
posicao_maior=[]

for p in range(0,5):
    val=int(input(f'digite um valor na posição {p}:'))
    lista.append(val)


for posicao,valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)

    if valores == min(lista):
        posicao_menor.append(posicao)

print(f'os valores digitados foram {lista}')
print(f'o maior valor valor digitado foi o {max(lista)} '
      f'na posição {posicao_maior}...outra forma de posição = ',end='')

#outra forma para a posição do MAIOR
for i , v in enumerate(lista):
    if v == max(lista):
        mai=i
        print(f'{mai}...',end='')
print()
print(f'o menor valor digitado foi o {min(lista)} '
      f'na posição {posicao_menor} outra forma de posição = ',end='')

#outra forma para a posição do MENOR
for i,v in enumerate(lista):
    if v ==min(lista):
        men=i
        print(f'{men}...',end='')
print()
