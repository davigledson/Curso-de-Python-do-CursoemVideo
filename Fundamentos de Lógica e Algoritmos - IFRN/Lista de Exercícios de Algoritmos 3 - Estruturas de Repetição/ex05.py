n=int(input('digite o numero base:'))
p=int(input('digite a numero expoente:'))
resu=1
for c in range(1,p+1):
    resu*=n
    print(f'{resu} X {resu} = {resu*n}')

