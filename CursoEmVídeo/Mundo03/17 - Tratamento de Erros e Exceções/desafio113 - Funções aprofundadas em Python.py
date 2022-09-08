def leiaint(num):
    while True:
        try:
            entrada=int(input(num))

        except KeyboardInterrupt:
            print('\033[;31;58mErro! Entrada de dados interrompida pelo usuario \033[m')
            return 0

        except (ValueError,TypeError):
            print('\033[;31;58mErro! Digite um numero inteiro valido\033[m')


        else:
            return entrada



def leiafloat(num):
    while True:
        try:
            entrada=float(input(num).replace(',','.'))
        except KeyboardInterrupt:
            print('\033[;31;58mErro! Entrada de dados interrompida pelo usuario \033[m')
            return 0

        except(ValueError,TypeError):
            print('\033[;31;58mErro! Digite um numero real valido\033[m')

        else:
            return entrada

a=leiaint('Digite um numero inteiro:')
b=leiafloat('Digite um numero Real:')

print(a)
print(b)