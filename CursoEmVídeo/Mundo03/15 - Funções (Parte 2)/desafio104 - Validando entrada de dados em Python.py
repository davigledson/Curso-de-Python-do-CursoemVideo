def leiaint(num):
    while True:
        resp=input(num)
        if resp.isnumeric() == True:
            return f'Voce acabou de digitar o numero {resp}' # o return funciona como um break tbm
        else:
            print('\033[;31;58mERRO! DIGITE UM NUMERO INTEIRO!\033[m')

fun=leiaint('Digite um numero:')
print(fun)