n1=soma=contador=0
while True:
    n1=int(input('Digite um valor (999 para pará):'))
    if n1 == 999:
        break

    soma+=n1
    contador+=1

print(f'a contagem de numeros digitados foi de {contador} e a soma entre eles foi de {soma}')