n1=input('digite algo:')
t=print('o tipo primitivo desse valor é ', type(n1))
a=print('e alfanumérico ? ',n1.isalnum())
b=print('e alfabético ? ', n1.isalpha())
c=print(' e numerico ? ' ,n1.isnumeric())
d=print('esta em maiúsculas ? ',n1.isupper())
e=print('esta em minúsculas ? ' ,n1.islower())
f=print('esta capitalizado ? ', n1.istitle())
g=print('só tem espaços ? ',n1.isspace())

# PODE SER FEITO ASSIM TAMBÉM

n2=input('digite algo:')
m=print(f'o tipo primitivo desse valor é {type(n1)}')
n=print(f'e alfanumérico ? {n1.isalnum()}')
v=print(f'e alfabético ? {n1.isalpha()}')
p=print(f' e numerico? {n1.isnumeric()}')
o=print(f'esta em maiúsculas ? {n1.isupper()}')
x=print(f'esta em minúsculas ? {n1.islower()}')
y=print(f'esta capitalizado ? {n1.istitle()}')
z=print(f'só tem espaços ? {n1.isspace()}')


