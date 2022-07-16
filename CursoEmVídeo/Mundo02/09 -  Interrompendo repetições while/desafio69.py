
f20=i18=hom=0
s='t'

while True:
    print('=='*20)
    print('CADASTRE UMA PESSOA')
    print('==' * 20)
    i = int(input('Idade:'))


    s = input('seu sexo [M/F]:').lower()
    while s !='m' and s!='f':
        s = input('seu sexo [M/F]:').lower()

    con=input('quer continuar [S/N]:').lower()
    while con != 's' and con!='n':
        con = input('quer continuar [S/N]:').lower()



    if s=='f' and i <=20:
        f20+=1
    if i >=18:
        i18+=1
    if s=='m':
        hom+=1
    if con =='n':
        break
print(f'o total de homens cadastrados foi de {hom}\no de mulheres com menos de 20 anos foi de {f20}\n e o de pessoas com +18 foi de {i18}')