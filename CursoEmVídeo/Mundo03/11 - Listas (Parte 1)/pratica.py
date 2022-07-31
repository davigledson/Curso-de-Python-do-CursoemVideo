num=[2,5,9,1]
num[2]=3
num.append(7) # adicionando
num.sort() # colocando em ordem

print(num)
num.sort(reverse=True) # ordem reversa
num.insert(2,0) # inserir elemento 2 = posição, 0 = elemento
print(num)

num.pop(2) # elimina o último elemento se não determinando
# eliminei o zero
print(num)

num.insert(2,2)
print(num)
num.remove(2)#remove a primiera ocorrencia do valor que vc determina

if 4 in num:
    num.remove(4)
else:
    print('não achei nenhum numero 4')
print(num)
print(f'essa lista tem {len(num)} elementos')