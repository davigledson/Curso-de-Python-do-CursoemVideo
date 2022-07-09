numero = int(input('Digite um Número para ver seu fatorial:'))
resultado=1
contador=1

while contador<=numero:
    resultado = resultado * contador
    contador = contador + 1
print(resultado)
print(contador)

