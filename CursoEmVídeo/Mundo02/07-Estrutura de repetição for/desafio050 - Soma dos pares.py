


contador=0
soma=0

for c in range(1,7):
    n1 = int(input(f'digite o {c}° numero:'))

    if n1%2==0:

        contador+=1
        soma+=n1
print('='*60)
print(f'a contagem dos selecionados e de {contador}')
print(f'a soma dos numeros pares e de selecionados e de {soma}')