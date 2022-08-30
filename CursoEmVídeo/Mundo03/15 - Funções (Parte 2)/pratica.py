def contador(i,f,p):
    #docstring usa aspas duplas
    """
    :param i: Inicio da contagem
    :param f:Fim da Contagem
    :param p:passo da contagem
    :return:sem renorno
    """
    c=i
    while c<=f:
        print(f'{c}',end=' ')
        c+=p
    print('Fim')

contador(-100,10,10)
help(contador)
print('='*20)

def somar(a=0,b=0,c=0):
    """

    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor

    função criada por Davi Gledson
    """
    s=a+b+c
    print(f'A soma vale {s}')

somar(1,2)
somar(9,5,8)
somar(8)

print('='*20)
help(somar)
def teste():
    x=8 # escopo local
    print(f'Na função teste,n vale {n}')
    print(f'Na função teste,x vale {x}')
print('='*20)

#programa principal
n=5 # escopo global
print(f'No programa princial n vale {n}')
teste()
#print(f'No programa princial x vale {x}')
print('='*20)
def funcao():
    global n1 # n1 local vai se comporta como global
    n1=4
    print(f'N1 dentro vale {n1}')

n1=7
funcao()
print(f'N1 fora vale {n1}')
print('=='*30)

def somar2(a=0,b=0,c=0):
    """

    :param a: O primeiro valor
    :param b: O segundo valor
    :param c: O terceiro valor
    :return = Soma de parametros
    função criada por Davi Gledson
    """
    s=a+b+c
    return s
num1=somar2(6,7,7)
num2=somar2(2,7,8)
num3=somar2(1,3,9)

print(f'Os resultados foram {num1}, {num2} e {num3}')

