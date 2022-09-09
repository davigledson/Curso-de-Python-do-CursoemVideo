#solução não entendida
import urllib.request


try:
    site=urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('O site pudin não esta acessivel no momento!')
else:
    print('Conseguir acessar o site com sucesso')
    print(site.read())

