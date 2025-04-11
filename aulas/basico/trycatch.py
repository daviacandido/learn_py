'''
Introdução ao Try/Except
========================

Try -> tenta executar o código
Except -> se der erro, executa o código do except
'''
numero_str = input('Digite um número para ser dobrado: ')

try:
    numero = float(numero_str)
    print(f'O dobro de {numero} é {numero*2}')
except ValueError:
    print("Isto não é um número")