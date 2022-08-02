termo=int(input('Digite o numero do termo:'))
ultimo=0
penutimo=1
for c in range(0,termo):
    termo=ultimo+penutimo
    penutimo=ultimo
    ultimo=termo

    print(termo)