maior=0
menor=0
for p in range(1,6):
    peso=float(input(f'digite o {p}° peso:').replace(',','.'))
    if p ==1:
        maior=peso
        menor=peso
    else:
        if maior<peso:
            maior=peso
        if menor>peso:
            menor=peso
print(f'o menor peso registrado foi {menor}Kg')
print(f'o menor peso registrado foi {maior}Kg')






