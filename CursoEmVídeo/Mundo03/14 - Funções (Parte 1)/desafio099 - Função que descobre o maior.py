def maior(*num):
    lista=[]
    for c in num:
        lista.append(c)
    for c in lista:
        print(f'{c}',end=' ')
    if len(lista) > 0:
        print(f'Foram informados e {len(lista)} ao todo.')
        print(f'O maior valor informado foi o {max(lista)}.')
    if len(lista)== 0:
        print(f'Nenhum valor foi informado')

def mostralinha():
    print('-=-'*20)
mostralinha()
maior(0,1,2,3,4,5)
mostralinha()

maior(6,4,5,6,9,8,7,4,54,69)

mostralinha()
maior(5,1,2,3,6,5,98)
mostralinha()
maior()

mostralinha()
maior(65,25,89,689,45)