import random

'''
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
'''

digito = random.randrange(25)
novo_digito = 1 if digito <= 9 else 0

print(novo_digito, digito)
