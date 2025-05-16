def exemplo():
    print('Este código está dentro de uma função.')


exemplo()

# Argumentos não nomeado:


def soma(x, y):
    print(f'A soma entre {x} e {y} é igual a {x + y}')


print(soma(1, 2))


# Argumentos não nomeados:


def subtracao(x, y):
    print(f'A subtração de {x} com {y} é igual a {x - y}')


subtracao(y=10, x=5)
