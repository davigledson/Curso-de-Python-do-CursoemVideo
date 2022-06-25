n1=float(input('digite o comprimento do cateto oposto:'))
n2=float(input('digite o comprimento do cateto adjacente:'))

print('seguindo a formula do teorema de pitágoras')
print('h² = ca² + co²')

s=n1**2 + n2**2
from math import sqrt
s2=sqrt(s)

print(f'a hipotenusa é igual a {s2:.2f}')

#outra forma mais facil de fazer
import math
r=math.hypot(n1 , n2)

print(f' o resultado é {r:.2f}')

