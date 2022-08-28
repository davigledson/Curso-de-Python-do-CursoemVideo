
def sorteio(lista):

    from random import randint
    for c in range(1,6):
        sor=randint(1,10)
        lista.append(sor)

    print(f'Os numeros sorteados foram ', end='')
    for c in lista:
        print(f'{c} ',end='')
    print()


def somapar(lista):
    lista_par=[]
    for c in lista:
        if c%2==0:
            lista_par.append(c)
    print(f'A soma dos numeros pares foram',end='',)
    soma=0
    for c in lista_par:
        soma+=c

        print(f' {c} ',end='')
    print(f' = {soma}')


numeros=[]
sorteio(numeros)
somapar(numeros)

