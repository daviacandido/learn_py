import os

# Calculadora

while True:
    os.system('clear')

    # Variaveis
    numero_1 = input('Insira o primeiro número: ')
    numero_2 = input('Insira o segundo número: ')
    operador = input('Insira um operador (+, -, *, /): ')

    numeros_validos = None

    # Verificacao de entradas do usuário:
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números inseridos são inválidos')
        continue

    if len(operador) == 0:
        print('Insira pelo menos um operador')
        continue

    if len(operador) > 1:
        print('Insira apenas um operador')
        continue

    operadores_validos = '+-*/'

    if operador not in operadores_validos:
        print('Operador inválido')
        continue

    # Calculos:
    print('Realizando os calculos: ')

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ',
              numero_1_float + numero_2_float)
    if operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ',
              numero_1_float - numero_2_float)
    if operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ',
              numero_1_float / numero_2_float)
    if operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ',
              numero_1_float * numero_2_float)

    # Verifica saida
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
