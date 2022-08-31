def par(num):
    if num %2==0:
        return True
    else:
        return False

n=int(input('Numero:'))
print(par(n))
if par(n):
    print('E par')
else:
    print('Não é par')