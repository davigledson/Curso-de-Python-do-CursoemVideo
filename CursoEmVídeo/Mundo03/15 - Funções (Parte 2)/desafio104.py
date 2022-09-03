def leiaint(num):
    while True:
        resp=input(num)


        if resp.isnumeric() == True:

            return f'Voce acabou de digitar o numero {resp}' # o return funciona como um break tbm


        else:
            print('ERRO! DIGITE UM NUMERO INTEIRO')

fun=leiaint('Digite um numero:')
print(fun)