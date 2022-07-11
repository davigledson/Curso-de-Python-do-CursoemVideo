n = input('Digite seu Sexo [M/F]:').lower().strip()[0]
while n not in 'MmFf':
# tbm pode ser assim = while n != 'm' and n != 'f':
    n = input('ERRO! Digite seu Sexo [M/F]:').lower().strip()[0]
print(f'SEXO {n} REGISTRADO COM SUSCESSO')




