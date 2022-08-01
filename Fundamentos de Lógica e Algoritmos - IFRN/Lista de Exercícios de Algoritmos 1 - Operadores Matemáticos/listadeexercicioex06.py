a=int(input('quantidade de votos validos para candidato A:'))
b=int(input('quantidade de votos validos para candidato B:'))
c=int(input('quantidade de votos validos para candidato C:'))
d=int(input('quantidade de votos nulos:'))
e=int(input('quantidade de votos em branco:'))
lt=a+b+c+d+e
ltv=a+b+c
eq1=(ltv*100)/lt
vbn=(d+e)*100/lt
va=(a)*100/lt
vb=(b)*100/lt
vc=(c)*100/lt

print(f'o numero total de eleitores foi de {a+b+c+d+e}')
print(f'o percentual correspondente de votos válidos em relação à quantidade de eleitores foi de {eq1:.1f}%')
print(f'percentual de votos brancos e votos nulos em relação à quantidade de eleitores foi de {vbn:.1f}%')

print((f'o percentual correspondente de votos válidos do candidato A, em relação à quantidade de eleitores totais foi de {va:.1f}%'))
print((f'o percentual correspondente de votos válidos do candidato B, em relação à quantidade de eleitores totais foi de {vb:.1f}%'))
print((f'o percentual correspondente de votos válidos do candidato C, em relação à quantidade de eleitores totais foi de {vc:.1f}%'))