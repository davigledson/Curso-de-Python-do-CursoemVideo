def mostrarlinha():
    print('-'*30)

def titulo(txt):
    print('='*30)
    print(txt)
    print('=' * 30)

# programa principal
titulo('Davi Gledson')

titulo('oi')

mostrarlinha()


def soma(a,b):
    s = a + b
    print(f'A = {a} B = {b}')
    print(f'{a} + {b} = {s}')

soma(5,6)
mostrarlinha()
soma(b=6,a=5)

mostrarlinha()
def contador(*num):
    print(num)
contador(5,5,6,5,4,7,8)
contador(9,2,4)
contador(6,6,4,5)

mostrarlinha()
def contador2(*num):
    for valor in num:
        print(f'{valor} ',end='')
    print('Fim')
contador2(5,5,6,5,4,7,8)
contador2(9,2,4)
contador2(6,6,4,5)

mostrarlinha()
def contador3(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')
contador3(5,5,6,5,4,7,8)
contador3(9,2,4)
contador3(6,6,4,5)

mostrarlinha()
valores=[0,1,2,3,4,5,6,7,8,9,10]
def dobra(lst):
    pos=0
    while pos<len(lst):
        lst[pos]*=2
        pos+=1

dobra(valores)
print(valores)

mostrarlinha()
def soma2(* valores):
    s=0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(1,2,3,4,5,6,7,8,9,10)
soma2(5,2)
