def executa(funcao, *args):
    return funcao(*args)


# transformar as seguintes funções em lambda:

i = 2
o = 3


def soma(x, y):
    return x + y


print(
    executa(
        lambda x, y: x + y,
        i, o
        )
    )


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa(
    lambda m: lambda n: n * m,
    3
)

print(
    executa(
        lambda *args: sum(args),
        2, 3, 4, 5, 6
    )
)

print(duplica(10))
