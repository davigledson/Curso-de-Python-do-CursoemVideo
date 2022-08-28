frase=input('\033[4;32m digite um frase:')
todas=frase.lower().strip().count('a')
fist=frase.lower().strip().find('a')+1
last=frase.lower().strip().rfind('a')+1

print(f'A letra ``a´´ aparece {todas} na frase')
print(f'A letra ``a´´ aparece primeiro na posição {fist}\n'
f' e por último na posição {last}')