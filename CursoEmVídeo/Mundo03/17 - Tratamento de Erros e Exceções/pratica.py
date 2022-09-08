try:
    a=int(input('Numerador:'))
    b=int(input('Denominador:'))
    r=a/b

#except Exception as erro:
    #print('Infelizmente tivemos um problema!')
    #print(f'O problema encontrado foi o {erro.__cause__}') O PROGRAMA DESCONSIDERA OS OUTROS EXCEPS,
# QUANDO O Exception e executado

except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que voce digitou.')

except ZeroDivisionError:
    print('Impossivel dividir por zero')

except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
else:
    print(f'resultado = {r}')
finally:
    print('Volte sempre!')