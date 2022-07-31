lista = []

while True:
    val = int(input('Digite um valor:'))



    if val in lista:
        print('valor duplicado! não vou adicionar!')
        lista.remove(val)

    else:
        print('Valor adicionado com sucesso')


    lista.append(val)

    esc=' '
    while esc not in 'sn':
        esc = input('Quer continuar?[S/N]:').lower()[0]

    if esc == 'n':
        break


print(f'Os numeros digitados foram {lista}')
print(f'Os valores digitados em ordem alfabetica é {sorted(lista)}')
