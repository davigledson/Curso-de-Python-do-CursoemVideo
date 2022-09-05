# codigo incompleto de proposito, continuar na proxima aula
def leiadinheiro(frase):

    while True:
        entrada=str(input(frase)).replace(',','.').strip()



        if entrada.isalpha() or entrada=="":
            print(f'\033[;31;58m ERRO: {entrada} é um preço invalido!\033[m')


        else:
            return  float(entrada)


