s=n=0
while True:
    n=int(input('DIGITE UM NUMERO:'))
    if n==999:
        break
    s+=n
print(f'a soma é {s}')

for c in range(0,5):
    print(c)