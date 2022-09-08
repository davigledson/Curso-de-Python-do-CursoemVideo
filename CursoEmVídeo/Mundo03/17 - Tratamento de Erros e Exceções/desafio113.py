def leiaint(num):
    while True:
        try:
            entrada=int(input(num))


        except KeyboardInterrupt:
            print('\033[;31;58mErro! o usuario decidiu interromper\033[m')
        except (ValueError,TypeError):
            print('\033[;31;58mErro! Digite um numero inteiro\033[m')

        else:
            return entrada


def leiafloat(num):
    while True:
        try:
            entrada=float(input(num))
        except KeyboardInterrupt:
            print('\033[;31;58mErro! O usuario decidiu interromper\033[m')
        except(ValueError,TypeError):
            print('\033[;31;58mErro! Digite um numero real\033[m')

        else:
            return entrada

a=leiaint('Digite um numero inteiro:')
b=leiafloat('Digite um numero Real:')

print(a)
print(b)