count = count_impar = 0

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
n3 = int(input('Digite mais um numero:'))
n4 = int(input('Digite o ultimo numero:'))

tupla = (n1, n2, n3, n4)
num9 = tupla.count(9)




print(f'Os numeros digitados foram {tupla}')
print(f'O numero 9 foi digitado {num9} vezes')

if 3 in tupla:
    num3 = tupla.index(3)
    print(f'O numero 3 aparece na posição {num3 + 1}° posição')
else:
    print('Não tem nenhum numero 3 na trufa')

for par in tupla:
    if par % 2 == 0:
        count += 1
    else:
        count_impar += 1
print(f"Os valores pares digitados foram {count}")
