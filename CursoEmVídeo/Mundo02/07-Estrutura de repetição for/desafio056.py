maior = 0
media = 0
sex = 0
fem = 0
masc = 0
fem20=0
nome=0
for nome in range(1, 5):
    print(  5*'=', f'{nome}° PESSOA', 5*'=')
    n = input('digite seu nome:')


    i = int(input('Qual sua idade:'))
    media += i


    s = input('sex=:H/F').lower()
    if 'h' in s:
        masc += 1
    if 'f' in s:
        fem += 1
    if 'f' in s and i>=20:
     fem20+=1

    if 'h' in s:

        if maior<i:
            maior=i
            nome=n


print('=' * 60)

medi = media / 4
print(f'a media de idade do grupo e de {medi} anos')
print(f'ha {fem} femeas e {masc} machos')
print(f'a quantidade de mulheres que ultrapassam a casa dos 20 anos é de  {fem20} mulheres')
print(f'o homem mais velho foi o {nome} com {maior} anos')
