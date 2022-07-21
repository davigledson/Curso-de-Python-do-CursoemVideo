lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'

# á parti do python 3.5 pode escrever sem os parenteses - Exemplo: lache = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#Tuplas são imutáveis
#lanche[1]= 'Refrigerante'
print(len(lanche))
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

print('='*20,'FOR 01','='*20)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

#outra maneira de for
print('='*20,'FOR 02','='*20)
for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('='*20,'FOR 03','='*20)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print(sorted(lanche))
print(lanche)

a=1,2,3
b=1,5,3,7
c=a+b

print(c)
print(len(c))
print(c.count(1))#contagem de isolados
print(c.index(5))#posição
print(c.index(1,1))