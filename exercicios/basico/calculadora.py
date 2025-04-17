# Calculadora

while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite qual o operador a ser usado (+-/*)')

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if len(operador) == 0:
        print('Digite um operador:')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue


    print('Realizando a sua conta, confira o resultado abaixo: ')
    
    if operador == '+':
        print(num_1_float + num_2_float)
    if operador == '-':
        print(num_1_float - num_2_float)
    if operador == '/':
        print(num_1_float / num_2_float)
    if operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Não deveria estar aqui.')


    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
