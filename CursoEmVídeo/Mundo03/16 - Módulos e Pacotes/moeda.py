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
    return f'R${num}'
