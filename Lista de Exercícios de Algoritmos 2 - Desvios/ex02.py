n1=float(input('Digite sua 1° nota:'))
n2=float(input('Digite sua 2° nota:'))
n3=float(input('Digite sua 3° nota:'))
n4=float(input('Digite sua 4° nota:'))

eq=(n1+n2+n3+n4)/4
if eq>=6:
    print(f'você foi APROVADO. Sua media foi {eq}')
if 5<=eq<6:
    print(f'voce foi ficou em RECUPERAÇÃO,sua media foi{eq}')
    r=int(input('digite sua nota de recuperação:'))
    if r>=3:
        print(f'PARABENS, VOCE FOI APROVADO! Sua media: {eq+ r/3}')
    if r<3:
        print(f'MEUS PESAMES, VOCE FOI REPROVADO! Sua media: {eq}')
if eq<5:
    print('voce foi REPROVADO')
