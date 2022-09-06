def metade(num=0,rs=False):

    if rs:
        return f'R${num/2}'
    else:
        return num / 2


def dobro(num=0,rs=False):
    if rs:
        return f'R${num*2}'
    else:
        return num*2

def aumentar(num=0,porcentagem=0,rs=False):
    if rs==True:
        return f'R${(porcentagem /100) *num + num}'
    else:
        return (porcentagem /100) *num + num

def diminuir(num=0,porcentagem=0,rs=False):
    if rs==True:
        return f'R${num-(porcentagem/100)*num}'
    else:
        return num-(porcentagem/100)*num

def moeda(num=0,moeda='R$'):

    return f'{moeda}{num:.2f}'.replace('.',',')


def resumo(num=0,aum=0,red=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do Preço: \t{dobro(num,True)}')
    print(f'Metade do preço: \t{metade(num,True)}')
    print(f'{aum}% de aumento: \t{aumentar(num,aum,True)}')
    print(f'{red}% de redução: \t{diminuir(num,red,True)}')
    print('-' * 30)

