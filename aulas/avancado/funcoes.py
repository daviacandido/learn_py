def exemplo():
    print('Este código está dentro de uma função.')


exemplo()

# Argumentos não nomeado:


def soma(x, y):
    print(f'A soma entre {x} e {y} é igual a {x + y}')


soma(2, 2)

# Argumentos não nomeados:


def subtracao(x, y):
    print(f'A subtração de {x} com {y} é igual a {x - y}')


subtracao(y=10, x=5)


# Argumentos padrão


def soma_3_numeros(x, y, z=None):
    if z is not None:
        print(f'A soma de {x} + {y} + {z} é igual a {x+y+z}')
    else:
        print(f'A soma de {x} + {y} é igual a {x+y}')


soma_3_numeros(2, 2, 2)
