from datetime import date
atual=date.today().year

totalmaior=0

totalmenor=0
for pess in range(1,8):


    n1 = int(input(f'em que ano a a {pess}° nasceu:'))
    nasc= atual - n1

    if nasc>=21:
        totalmaior +=1

    else:
        totalmenor +=1

print(f'Ao todo tivemos {totalmenor} menores de idade')
print(f'E {totalmaior} maiores de idade')