lista=[]
posicao_menor=[]
posicao_maior=[]

for p in range(0,5):
    val=int(input(f'digite um valor na posição {p}:'))
    lista.append(val)
print(lista)

for posicao,valores in enumerate(lista):
    if valores == max(lista):
        posicao_maior.append(posicao)

    if valores == min(lista):
        posicao_menor.append(posicao)

print(f'os valores digitados foram {lista}')
print(f'o maior valor valor digitado foi o {max(lista)} na posição {posicao_maior}...')
print(f'o menor valor digitado foi o {min(lista)} na posição {posicao_menor}')

