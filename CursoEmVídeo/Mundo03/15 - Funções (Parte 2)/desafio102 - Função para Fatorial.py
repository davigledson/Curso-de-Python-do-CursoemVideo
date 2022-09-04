def fatorial(num,show=False):
    """

     -> Calcula o Fatorial de un número

    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não o calculo
    :return: O valor do fatorial do numero num
    """
    f=1
    for c in range(num,0,-1):
        f = f * c
        if show==True:
            print(f' {c} ', end='')
            if c != 1:
                print('x', end='')
    if show==True:
        return (f'= {f}')

    return f


print(fatorial(5))
print('=='*20)

n=fatorial(5,True)
print(n)

print('=='*20)

print(fatorial(7,True))

print('=='*20)
help(fatorial)
