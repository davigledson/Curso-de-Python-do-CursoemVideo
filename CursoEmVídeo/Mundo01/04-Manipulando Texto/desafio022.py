nome=input('digite seu nome completo:')
print('esse e o seu nome digitado corretamente')
print(nome.title())

print('esse e seu nome com todas as letras maiúsculas')
print(nome.upper())

print('esse e seu nome com todas as letras minúsculas ')
print(nome.lower())

print('esse e a quantidade de letras que seu nome completo tem (sem os espaços)')
a=(nome.split())
b=(''.join(a))
print(len(b))

#outra formas
print(len(nome.replace(' ', '')))
print(len(nome) -nome.count(' '))

print(f'o seu primeiro nome é {nome.split()[0]} e a quantidade de letras que seu  primeiro nome tem é')
print(len(nome.split()[0]))