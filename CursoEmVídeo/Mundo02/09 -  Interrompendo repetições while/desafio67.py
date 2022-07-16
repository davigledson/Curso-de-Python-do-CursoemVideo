soma=mult=div=sub=cont=0



while True:
    n1 = int(input('Que ver a tabuada de qual valor?'))
    if n1 <0:
        break
    for c in range(1,11):
        print(f'MUTIPLICAÇÂO -> {n1} x {c} = {n1*c}',f'DIVISÂO -> {n1} / {c} = {n1/ c}',f'SOMA -> {n1} + {c} = {n1+c}',f'SUBTRAÇÂO -> {n1}- {c} = {n1-c}')




