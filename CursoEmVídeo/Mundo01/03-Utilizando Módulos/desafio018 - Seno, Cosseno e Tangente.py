n1=float(input('digite o ângulo que você deseja:'))
import math
a=math.radians(n1)
seno=math.sin(a)

b=math.radians(n1)
cosseno=math.cos(a)

c=math.radians(n1)
tangente=math.tan(c)


print(f'o ângulo de {n1} tem o SENO de {seno:.2f}')
print(f'o ângulo de {n1} tem o COSSENO de {cosseno:.2f}')
print(f'o ângulo de {n1} tem a TANGENTE de {tangente:.2f}')

#outra forma com menos linhas
seno2=math.sin(math.radians(n1))
print(f'{seno2:.2f}')
cosseno2=math.cos(math.radians(n1))
print(f'{cosseno2:.2f}')
tangente2=math.tan(math.radians(n1))
print(f'{tangente2:.2f}')
#sobre o (),lembre-se da ordem de precedencia