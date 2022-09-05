def metade(num,rs=False):

    if rs:
        return f'R${num/2}'
    else:
        return num / 2


def dobro(num,rs=False):
    if rs:
        return f'R${num*2}'
    else:
        return num*2

def aumentar(num,porcentagem,rs=False):
    if rs==True:
        return f'R$ {(porcentagem /100) *num + num}'
    else:
        return (porcentagem /100) *num + num

def diminuir(num,porcentagem,rs=False):
    if rs==True:
        return f'R${num-(porcentagem/100)*num}'
    else:
        return num-(porcentagem/100)*num

def moeda(num):

    return f'R${num:.2f}'.replace('.',',')

def resumo(num,aum,red):
    print('--'*19)
    print('         RESUMO DO VALOR')
    print('--'*19)
    print('--' * 19)
    print(f'Preço analidado: R${num}')
    print(f'Dobro do Preço: R${num*2}')
    print(f'Metade do preço: R${num/2}')
    print(f'{aum}% de aumento: R${(aum /100) *num + num}')
    print(f'{red}% de redução: R${num-(red/100)*num}')
    print('--' * 19)

