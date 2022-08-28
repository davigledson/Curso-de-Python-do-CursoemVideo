
f20=i18=hom=0


while True:
    print('=='*20)
    print('CADASTRE UMA PESSOA')
    print('==' * 20)
    i = int(input('Idade:'))


    s=' '
    while s not in 'MmFf':
        s = input('seu sexo [M/F]:').lower().strip()[0]

    con=' '
    while con not in 'SsNn':
        con = input('quer continuar [S/N]:').lower()



    if s=='f' and i <=20:
        f20+=1
    if i >=18:
        i18+=1
    if s=='m':
        hom+=1
    if con =='n':
        break
print(f'o total de homens cadastrados foi de {hom}\no de mulheres com menos de 20 anos foi de {f20}\no de pessoas com +18 foi de {i18}')