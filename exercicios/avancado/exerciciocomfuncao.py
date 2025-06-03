# Exercicio com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável


def multiplica(*args):
    total = 1
    numeros_multiplicacao = []
    try:
        for numeros in args:
            numeros_multiplicacao.append(float(numeros))
    except ValueError:
        return "Insira apenas números"
    for numeros in numeros_multiplicacao:
        total *= numeros
    return total

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar


def par_ou_impar(numero):
    try:
        numero_int = int(numero)
    except ValueError:
        return "Insira um número inteiro"

    if numero_int % 2 == 0:
        return f"{numero_int} é par"
    return f"{numero_int} é impar"


verifica_par_impar = par_ou_impar(7)
multiplicacao = multiplica(2, 2, 2)

print(verifica_par_impar)
print(multiplicacao)
