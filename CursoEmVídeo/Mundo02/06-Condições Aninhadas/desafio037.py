n1=int(input('digite um numero:'))

print('digite [1] para converter em binario')
print('digite [2] para converter em hexadecimal')
print('digite [3] para converter em octal')
a=(input('sua opção:'))

if str(1) in a:
    print(bin(n1)[2:])

elif str (2) in a:
    print(hex(n1)[2:])
elif  str(3) in a:
    print(oct(n1)[2:])
else:
    print('opção invalida')