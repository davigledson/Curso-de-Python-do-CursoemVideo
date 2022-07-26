print('='*20,'ligação','='*20)
a=[2,3,4,7]
b=a
b[2]=8 #não estar fazendo copia, mas assim uma ligação

print(a)
print(b)

print('='*20,'copia','='*20)

a1=[2,3,4,7]
print(a1)
c=a1[:] # fazendo copia corretamente da lista
c[2]=8
print(c)