#i=int(input('digite o inicio:'))
#f=int(input('digite o final'))
#p=int(input('digite o passo:'))
soma=0
contador=0
for a in range(1,501,2):
    if a %3==0:
        soma+=a
        contador+=1
print(f'a contagem dos numeros solicitados e de {contador} ')

print(f'a soma de todo os valores solicitados é {soma}')
