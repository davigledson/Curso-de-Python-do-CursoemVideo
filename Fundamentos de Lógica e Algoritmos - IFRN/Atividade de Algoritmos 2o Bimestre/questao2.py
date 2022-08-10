''' Elabore um questionario de 3 questões com 10 alternativas e que contenha 3 alternativas corretas
 '''
from time import sleep
print('Qual linguagem não é de programação?')
print('[1] - Python'),sleep(.5)
print('[2] - JavaScrip'),sleep(.5)
print('[3] - Piton'),sleep(.5)
print('[4] - Java'),sleep(.5)
print('[5] - Ruby'),sleep(.5)
print('[6] - Css'),sleep(.5)
print('[7] - PHP'),sleep(.5)
print('[8] - C++'),sleep(.5)
print('[9] - Html'),sleep(.5)
print('[10] - Assembly'),sleep(.5)

l=int(input('selecione uma opção:'))
if l == 3 or l==6 or l ==9:
    print('='*10,'Alternativa Correta!','='*10,)
else:
    print('='*10,'Alternativa errada!','='*10)

print('De acordo com o IMDB (Internet Movie Database) selecione a alternativa '
      'que pertença ao top 3ª das serie mais bem avaliadas do mundo ')

print('[1] - Friends'),sleep(.5)
print('[2] - Game of Thrones'),sleep(.5)
print('[3] - Black Mirror'),sleep(.5)
print('[4] - Breaking Bad'),sleep(.5)
print('[5] - Peaky Blinders'),sleep(.5)
print('[6] - Chernobyl'),sleep(.5)
print('[7] -O Gambito da Rainha'),sleep(.5)
print('[8] - Stranger Things'),sleep(.5)
print('[9] - House of Cards'),sleep(.5)
print('[10] - Better Call Saul'),sleep(.5)

s=int(input('Selecione uma opção:'))
if s ==2 or s==4 or s==6:
    print('='*10,'Alternativa correta!','='*10)
else:
    print('='*10,'Alternativa Errada!','='*10)

print('selecione uma das HQs entre as 3ª tops HQs mais bem mais avaliadas de todos os tempos')
print('[1] - “Batman – Ano um”, de Frank Miller e David Mazzucchelli'),sleep(.5)
print('[2] - “V de vingança”, de Alan Moore e David Lloyd'),sleep(.5)
print('[3] - “Sandman: estação das brumas”, de Neil Gaiman, Kelley Jones, Dick Giordano, e outros'),sleep(.5)
print('[4] - “Batman – A Piada Mortal”, de Alan Moore, Brian Bolland e John Higgins'),sleep(.5)
print('[5] - “Born again” (Demolidor), de Frank Miller e David Mazzucchelli'),sleep(.5)
print('[6] - “Guerra civil” (Vingadores), de Mark Millar, Steve McNiven e Dexter Vines'),sleep(.5)
print('[7] - “A saga da Fênix Negra”, de Chris Claremont, John Byrne e Terry Austin'),sleep(.5)
print('[8] - ”Reino do amanhã”, de Mark Waid e Alex Ross'),sleep(.5)
print('[9] - “Watchmen”, de Alan Moore e Dave Gibbons'),sleep(.5)
print('[10] - “Crise nas infinitas terras”, de Marv Wolfman, George Perez, Dick Giordano e Jerry Ordway'),sleep(.5)

h=int(input('Selecione uma opção:'))
if h == 5 or h==7 or h==9:
    print('='*10,'Alternativa Correta!','='*10,)
else:
    print('='*10,'Alternativa Errada!','='*10,)
